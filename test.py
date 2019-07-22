try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("导入 RPi.GPIO 时出现错误！这可能由于没有超级用户权限造成的。您可以使用 'sudo' 来运行您的脚本。")
