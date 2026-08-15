def main():
    spacecraft = {"name": "James Web Space Telescope"}
    spacecraft["distance"] = 0.01
    print(create_report(spacecraft))


def create_report(spacecraft):
    return f"""
    ========== RETURN =========

    Name: {spacecraft["name"]}
    Distance: {spacecraft["distance"]} AU

    ============================
    """

main()
