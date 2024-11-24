import ux
import re 

class Map:

    def __init__(self, file_path, objects_path=None):
        with open(file_path, 'r') as f:
            self.map_data = [list(line.strip()) for line in f.readlines()]
        
        self.object_data = [row[:] for row in self.map_data] #OBJECT Layer (NPC and ITEMS)
        self.player_position = self.find_player()
        self.objects = self.load_objects(objects_path) if objects_path else {}

    def find_player(self):
        for y, row in enumerate(self.map_data):
            for x, cell in enumerate(row):
                if cell == 'P':
                    return (x, y)
        raise ValueError("Player starting position not found on the map.")
    
    def load_objects(self, objects_path):
        objects = {}
        with open(objects_path, 'r') as f:
            category = None
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if line.startswith('{') and line.endswith('}'):
                    category = line.strip('{}')
                elif category and ':' in line:
                    coords, message = line.split(':', 1)
                    coords = tuple(map(int, coords.strip('()').split(',')))  # Parse (x, y)
                    objects[coords] = (category, message.strip())
        return objects

    def display_map(self):
        for y, row in enumerate(self.map_data):
            formatted_row = ''.join(
                f"{ux.EM}{cell}{ux.RST}" if cell == 'P' else
                f"{ux.OBJ}{cell}{ux.RST}" if cell == 'T' else
                f"{ux.NPC}{cell}{ux.RST}" if cell == 'N' else
                f"{ux.WALL}{cell}{ux.RST}" if cell == '#' else
                cell for cell in row
            )
            print(formatted_row)

    def format_message(self, message):
        def replace_keyword(match):
            keyword = match.group(1)
            return f"{ux.EM}{keyword}{ux.RST}"
    
    def is_move_valid(self, new_x, new_y):
        if 0 <= new_y < len(self.map_data) and 0 <= new_x < len(self.map_data[0]): # Check if new position is within the map
            return self.map_data[new_y][new_x] not in ['#'] # Check if new position is not a wall
        return False
    
    def move_player(self, direction):
        x, y = self.player_position
        if direction.upper() == 'N':
            new_x, new_y = x, y - 1
            direction_full = 'north'
        elif direction.upper() == 'S':
            new_x, new_y = x, y + 1
            direction_full = 'south'
        elif direction.upper() == 'E':
            new_x, new_y = x + 1, y
            direction_full = 'east'
        elif direction.upper() == 'W':
            new_x, new_y = x - 1, y
            direction_full = 'west'
        else:
            return False, "Invalid direction!"
        
        if self.is_move_valid(new_x, new_y):
            # Restore OBJECT layer
            self.map_data[y][x] = self.object_data[y][x]
            # Update map: clear old position and move 'P' to the new position
            self.map_data[new_y][new_x] = 'P'
            self.player_position = (new_x, new_y)

            # Check if there's an object at the new position
            if (new_x, new_y) in self.objects:
                category, message = self.objects[(new_x, new_y)]
                if category == 'CELLS':
                    return True, self.format_message(message)
                elif category == 'NPCS':
                    return True, f"You encounter {self.format_message(message)}!"
                elif category == 'ITEMS':
                    return True, f"You found {self.format_message(message)}!"
            
            return True, f"You move {direction}."
        else:
            return False, "You can't move there!"