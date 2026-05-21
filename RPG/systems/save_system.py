import json
import os
from datetime import datetime

SAVE_FILE = "saves/savegame.json"


def _item_to_dict(item):
    if item is None:
        return None
    base = {
        "id": item.id,
        "name": item.name,
        "image": item.image,
        "cost": item.cost,
        "rareness": item.rareness,
        "required_level": item.required_level,
        "max_stack": item.max_stack,
        "type": item.item_type(),
    }
    item_type = item.item_type()
    if item_type == "Weapon":
        base["damage"] = item.damage
    elif item_type == "Armor":
        base["defense"] = item.defense
    elif item_type == "Potion":
        base["mana_restore"] = item.mana_restore
    elif item_type == "Food":
        base["health_restore"] = item.health_restore
    elif item_type == "Backpack":
        base["capacity"] = item.capacity
    return base


def _dict_to_item(data):
    if data is None:
        return None
    from systems.Items import Weapon, Armor, Potion, Food, Backpack
    item_type = data.get("type")
    kwargs = dict(
        id=data["id"],
        name=data["name"],
        image=data["image"],
        cost=data["cost"],
        rareness=data["rareness"],
        required_level=data["required_level"],
        max_stack=data.get("max_stack", 1),
    )
    if item_type == "Weapon":
        return Weapon(**kwargs, damage=data["damage"])
    elif item_type == "Armor":
        return Armor(**kwargs, defense=data["defense"])
    elif item_type == "Potion":
        return Potion(**kwargs, mana_restore=data["mana_restore"])
    elif item_type == "Food":
        return Food(**kwargs, health_restore=data["health_restore"])
    elif item_type == "Backpack":
        return Backpack(**kwargs, capacity=data["capacity"])
    return None


def save_game(player_stats, inventory, save_path=SAVE_FILE):
    try:
        os.makedirs(os.path.dirname(save_path) or ".", exist_ok=True)

        stats_data = {
            "level": player_stats.level,
            "xp": player_stats.xp,
            "xp_to_next_level": player_stats.xp_to_next_level,
            "current_hp": player_stats.current_hp,
            "max_hp": player_stats.max_hp,
            "current_mana": player_stats.current_mana,
            "max_mana": player_stats.max_mana,
            "base_hp": player_stats._base_hp,
            "base_mana": player_stats._base_mana,
            "base_attack": player_stats._base_attack,
            "base_defense": player_stats._base_defense,
            "speed": player_stats._speed,
            "attack_range": player_stats._attack_range,
            "crit_chance": player_stats._crit_chance,
        }

        # Позиция игрока
        position_data = {
            "x": float(player_stats.pos_x),
            "y": float(player_stats.pos_y),
        }

        inventory_data = {
            "equipped": {
                "weapon": _item_to_dict(inventory.equipped.get("weapon")),
                "armor":  _item_to_dict(inventory.equipped.get("armor")),
            },
            "potions": [_item_to_dict(p) for p in (inventory.potion or [])],
            "slots":   [_item_to_dict(item) for item in inventory.slots],
        }

        save_data = {
            "meta": {
                "saved_at": datetime.now().isoformat(timespec="seconds"),
                "version": "1.1",
            },
            "position": position_data,
            "stats": stats_data,
            "inventory": inventory_data,
        }

        with open(save_path, "w", encoding="utf-8") as f:
            json.dump(save_data, f, ensure_ascii=False, indent=2)

        print(f"[SaveSystem] Игра сохранена -> {save_path}")
        return True

    except Exception as e:
        print(f"[SaveSystem] Ошибка сохранения: {e}")
        return False


def load_game(player_stats, inventory, save_path=SAVE_FILE):
    if not os.path.exists(save_path):
        print(f"[SaveSystem] Файл не найден: {save_path}")
        return False

    try:
        with open(save_path, "r", encoding="utf-8") as f:
            save_data = json.load(f)

        # Статы
        s = save_data["stats"]
        player_stats._level           = s["level"]
        player_stats.xp               = s["xp"]
        player_stats._xp_to_next_level = s["xp_to_next_level"]
        player_stats._base_hp         = s["base_hp"]
        player_stats._base_mana       = s["base_mana"]
        player_stats._base_attack     = s["base_attack"]
        player_stats._base_defense    = s["base_defense"]
        player_stats._max_hp          = s["max_hp"]
        player_stats._max_mana        = s["max_mana"]
        player_stats.current_hp       = s["current_hp"]
        player_stats.current_mana     = s["current_mana"]
        player_stats._attack          = int(s["base_attack"] * 1.15 * s["level"])
        player_stats._defense         = int(s["base_defense"] * 1.10 * s["level"])
        player_stats._speed           = s["speed"]
        player_stats._attack_range    = s["attack_range"]
        player_stats._crit_chance     = s["crit_chance"]

        # Позиция игрока
        if "position" in save_data:
            pos = save_data["position"]
            player_stats.pos_x = pos["x"]
            player_stats.pos_y = pos["y"]
            player_stats.rect.center = (int(pos["x"]), int(pos["y"]))
            player_stats.target_pos = None

        # Инвентарь
        inv = save_data["inventory"]
        inventory.equipped["weapon"] = _dict_to_item(inv["equipped"]["weapon"])
        inventory.equipped["armor"]  = _dict_to_item(inv["equipped"]["armor"])
        inventory.potion = [
            _dict_to_item(p) for p in inv.get("potions", []) if p is not None
        ]
        loaded_slots = inv.get("slots", [])
        inventory.slots = [None] * 32
        for i, item_data in enumerate(loaded_slots[:32]):
            inventory.slots[i] = _dict_to_item(item_data)

        saved_at = save_data.get("meta", {}).get("saved_at", "?")
        print(f"[SaveSystem] Загружено ({saved_at})")
        return True

    except (KeyError, json.JSONDecodeError) as e:
        print(f"[SaveSystem] Ошибка загрузки: {e}")
        return False


def save_exists(save_path=SAVE_FILE):
    return os.path.exists(save_path)


def delete_save(save_path=SAVE_FILE):
    try:
        if os.path.exists(save_path):
            os.remove(save_path)
            return True
        return False
    except Exception as e:
        print(f"[SaveSystem] Ошибка удаления: {e}")
        return False
