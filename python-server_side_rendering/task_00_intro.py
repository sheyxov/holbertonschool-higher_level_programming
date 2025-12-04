# task_00_intro.py

def generate_invitations(template, attendees):
    # Input tipi yoxlama
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Boş template
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Boş siyahı
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Hər iştirakçı üçün fayl yaratma
    for index, attendee in enumerate(attendees, start=1):
        # Məlumat əgər yoxdur və ya None-dırsa N/A yaz
        name = attendee.get("name") or "N/A"
        event_title = attendee.get("event_title") or "N/A"
        event_date = attendee.get("event_date") or "N/A"
        event_location = attendee.get("event_location") or "N/A"

        # Placeholder-ların dəyişdirilməsi
        output_text = (template.replace("{name}", name)
                                .replace("{event_title}", event_title)
                                .replace("{event_date}", event_date)
                                .replace("{event_location}", event_location))

        # Fayl yazma
        filename = f"output_{index}.txt"
        with open(filename, "w") as file:
            file.write(output_text)

        print(f"Generated: {filename}")
