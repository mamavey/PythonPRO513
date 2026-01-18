"""
Тип ошибки 4: Виртуальная среда не активируется

Команда activate (активации) виртуальной среды не работает.

Пример ошибки: см. файл Mistake_04_example.png
"""

"""
Решение:
1) На Windows включим разрешение на выполнение скриптов
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
(запускать powershell от имени администратора)
2) Убедимся, что правильно указан путь к activate
.\\.venv\\Scripts\\activate
"""
