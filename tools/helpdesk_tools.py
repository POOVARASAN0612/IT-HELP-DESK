from datetime import datetime


def get_system_status():
    """
    Simulated system-status tool.
    """

    return {
        "status": "Online",
        "checked_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "message": (
            "IT Helpdesk service is available."
        )
    }


def create_support_ticket(issue):
    """
    Simulated support-ticket creation tool.
    """

    ticket_id = (
        "IT-"
        + datetime.now().strftime(
            "%Y%m%d%H%M%S"
        )
    )

    return {
        "ticket_id": ticket_id,
        "issue": issue,
        "status": "Created",
        "message": (
            "Your issue has been recorded "
            "for IT support."
        )
    }


# --------------------------------------------------
# TEST TOOLS
# --------------------------------------------------

if __name__ == "__main__":

    print("System Status:")
    print(get_system_status())

    print("\nSupport Ticket:")
    print(
        create_support_ticket(
            "Unable to connect to Wi-Fi"
        )
    )
