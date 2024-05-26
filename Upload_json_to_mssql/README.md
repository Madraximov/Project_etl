# ETL



## First task

Objective: Design and implement a simple ETL (Extract, Transform, Load) pipeline for a sample dataset

In my first task I prefer use AirFlow, I created a DAG with tem

# EER Diagram for ClickData Table

The EER diagram represents the structure of the `ClickData` table, which stores click event data.

# ClickData Table Documentation

## Table: ClickData

The `ClickData` table stores information about click events, including metadata about the device, location, and user agent.

### Columns

| Column              | Type          | Description                                 |
|---------------------|---------------|---------------------------------------------|
| application_id      | VARCHAR(50)   | ID of the application.                      |
| publisher_name      | VARCHAR(255)  | Name of the publisher.                      |
| publisher_id        | VARCHAR(50)   | ID of the publisher.                        |
| tracker_name        | VARCHAR(255)  | Name of the tracker.                        |
| tracking_id         | VARCHAR(255)  | Tracking ID.                                |
| click_timestamp     | BIGINT        | Timestamp of the click event.               |
| click_datetime      | DATETIME      | Datetime of the click event.                |
| click_ipv6          | VARCHAR(50)   | IPv6 address of the click.                  |
| click_url_parameters| VARCHAR(MAX)  | URL parameters of the click.                |
| click_id            | VARCHAR(50)   | ID of the click.                            |
| click_user_agent    | VARCHAR(MAX)  | User agent string of the click.             |
| ios_ifa             | VARCHAR(50)   | iOS Identifier for Advertisers.             |
| ios_ifv             | VARCHAR(50)   | iOS Identifier for Vendors.                 |
| android_id          | VARCHAR(50)   | Android ID.                                 |
| google_aid          | VARCHAR(50)   | Google Advertising ID.                      |
| os_name             | VARCHAR(50)   | Name of the operating system.               |
| os_version          | VARCHAR(50)   | Version of the operating system.            |
| device_manufacturer | VARCHAR(50)   | Manufacturer of the device.                 |
| device_model        | VARCHAR(50)   | Model of the device.                        |
| device_type         | VARCHAR(50)   | Type of the device (e.g., phone, tablet).   |
| is_bot              | VARCHAR(10)   | Indicates if the user is a bot (true/false).|
| country_iso_code    | VARCHAR(10)   | ISO code of the country.                    |
| city                | VARCHAR(50)   | City of the click event.                    |

### Description

- **application_id:** This colstores the unique ID of the application from which the click event originated.
- **publisher_name:** This column stores the name of the publisher responsible for the ad click.
- **publisher_id:** This column stores the unique ID of the publisher.
- **tracker_name:** This column stores the name of the tracker used to track the click event.
- **tracking_id:** This column stores the unique ID used for tracking the click event.
- **click_timestamp:** This column stores the Unix timestamp of the click event.
- **click_datetime:** This column stores the human-readable datetime of the click event.
- **click_ipv6:** This column stores the IPv6 address from which the click event was made.
- **click_url_parameters:** This column stores any URL parameters associated with the click event.
- **click_id:** This column stores the unique ID of the click event.
- **click_user_agent:** This column stores the user agent string of the device that made the click.
- **ios_ifa:** This column stores the iOS Identifier for Advertisers, if available.
- **ios_ifv:** This column stores the iOS Identifier for Vendors, if available.
- **android_id:** This column stores the Android ID, if available.
- **google_aid:** This column stores the Google Advertising ID, if available.
- **os_name:** This column stores the name of the operating system on the device that made the click.
- **os_version:** This column stores the version of the operating system on the device that made the click.
- **device_manufacturer:** This column stores the manufacturer of the device that made the click.
- **device_model:** This column stores the model of the device that made the click.
- **device_type:** This column stores the type of the device (e.g., phone, tablet) that made the click.
- **is_bot:** This column indicates whether the click event was made by a bot (true/false).
- **country_iso_code:** This column stores the ISO code of the country from which the click event was made.
- **city:** This column stores the city from which the click event was made.
