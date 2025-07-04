import sys
from datetime import datetime, timedelta
from tasks.bot import AddressBook, Record

def main():
    print("========== Address Book OOP Demo ==========")
    book = AddressBook()

    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    john_record.add_birthday("25.12.1990")

    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    today = datetime.now()
    next_week = today + timedelta(days=5)
    jane_record.add_birthday(next_week.strftime("%d.%m.%Y"))
    book.add_record(jane_record)

    print("\nAll contacts:")
    for name, record in book.data.items():
        print(record)

    john = book.find("John")
    if john:
        john.edit_phone("1234567890", "1112223333")
        print(f"\nAfter editing John's phone:\n{john}")

        found_phone = john.find_phone("5555555555")
        if found_phone:
            print(f"\nFound phone for {john.name}: {found_phone}")

    print("\nUpcoming birthdays:")
    upcoming = book.get_upcoming_birthdays()
    if upcoming:
        for item in upcoming:
            print(f"  {item['name']}: {item['congratulation_date']}")
    else:
        print("  No birthdays in the next week")

    book.delete("Jane")
    print("\nAfter deleting Jane:")
    for name, record in book.data.items():
        print(record)

    print("\n" + "="*50)
    print("To run the interactive bot, execute:")
    print("  python3 tasks/bot.py")
    print("\nAvailable commands:")
    print("  hello - greet the bot")
    print("  add <name> <phone> - add new contact or phone")
    print("  change <name> <old_phone> <new_phone> - change phone")
    print("  phone <name> - show phones for contact")
    print("  all - show all contacts")
    print("  add-birthday <name> <DD.MM.YYYY> - add birthday")
    print("  show-birthday <name> - show birthday")
    print("  birthdays - show upcoming birthdays")
    print("  delete <name> - delete contact")
    print("  close/exit - exit the bot")


if __name__ == "__main__":
    sys.exit(main())
