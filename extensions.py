def main():
    file_extension = input("File name: ").strip().lower()


    if file_extension.endswith(".gif"):
            print("image/gif")
    if file_extension.endswith(".jpg"):
            print("image/jpeg")
    if file_extension.endswith(".jpeg"):
            print("image/jpeg")
    if file_extension.endswith(".png"):
            print("image/png")
    if file_extension.endswith(".pdf"):
            print("application/pdf")
    if file_extension.endswith(".txt"):
            print("text/plain")
    if file_extension.endswith(".zip"):
            print("application/zip")


    if not(file_extension.endswith(".gif")):
        if not(file_extension.endswith(".jpg")):
            if not(file_extension.endswith(".jpeg")):
                if not(file_extension.endswith(".png")):
                    if not(file_extension.endswith(".pdf")):
                        if not(file_extension.endswith(".txt")):
                            if not(file_extension.endswith(".zip")):
                                print("application/octet-stream")


main()
