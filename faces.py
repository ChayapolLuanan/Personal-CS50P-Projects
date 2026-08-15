def main():
    message = input()
    final_message = convert(message )
    print(final_message)

def convert(message):
    smile_message =  message.replace(':)', '🙂')
    smile_frowning_message = smile_message.replace(':(', '🙁')
    return smile_frowning_message

main()
