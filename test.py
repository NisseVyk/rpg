def on_press(key):
    print('{0}'.format(
        key))



# Collect events until released
with Listener(
        on_press=on_press) as listener:
    listener.join()



