try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("���� RPi.GPIO ʱ���ִ������������û�г����û�Ȩ����ɵġ�������ʹ�� 'sudo' ���������Ľű���")
