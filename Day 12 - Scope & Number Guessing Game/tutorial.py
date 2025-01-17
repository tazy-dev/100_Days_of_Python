# Global Scope
enemies = 1
def increaseEnemies():
    # Local Scope
    enemies = 2
    print(f'enemies inside functoin : {enemies}')

increaseEnemies()
print(f'enemies outside functoin : {enemies}')

# Modefing Global
def increaseGlobalEnemies():
    global enemies
    # refrencing the global value
    enemies = 2
    print(f'enemies inside functoin : {enemies}')

increaseGlobalEnemies()
print(f'enemies outside functoin : {enemies}')

# Global Constants : Defined all caps
PI = 3.14