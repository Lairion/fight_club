from pathlib import Path
# __file__ це відносний шлях та ім'я файлу
# .resolve() перетворює відносний шлях на абсолютний
# .parent повертає значення Path що зберігає шлях до папки у якій знаходиться цей файл
BASE_DIR = Path(__file__).resolve().parent