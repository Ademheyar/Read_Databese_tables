Certainly! Here's an updated version of the README text with the requested changes:

# Database Viewer

This is a simple Python application that allows you to view the contents of an SQLite database using a tabbed interface. The application was developed using the Tkinter and SQLite3 modules.

## Getting Started

To use this application, you will need to have Python 3 and the following modules installed:

- Tkinter
- SQLite3

Once you have installed these modules, you can run the application by executing the following command in your terminal:

```
python database_viewer.py
```

This will launch the application and display the main window.

## Features

- View the contents of an SQLite database using a tabbed interface
- Each tab displays the contents of a different table in the database
- Vertical and horizontal scrollbars are added to each tableview widget to ensure all contents can be seen
- Set minimum tab width and adds scrollbar for tab names if there are more tabs than can fit

## How to Use

1. Launch the application by running the `database_viewer.py` file.
2. The application will automatically connect to the specified SQLite database.
3. A tabbed interface will be displayed, with each tab corresponding to a different table in the database.
4. Click on a tab to view the contents of the corresponding table.
5. Scroll vertically and horizontally to see all contents.
6. If there are more tabs than can fit in the available space, use the scrollbar at the bottom to navigate to the other tabs.

## Future Enhancements

Here are some potential enhancements that could be made to the application in the future:

- Allow users to search for specific records within a table.
- Add support for editing and updating records in the database.
- Implement sorting functionality for columns in the table view.
- Improve the user interface design for a more visually appealing experience.
- Add export options to save table data in various formats (e.g., CSV, Excel).
- Support multiple database connections and switch between them dynamically.

## Contributing

Contributions to this project are welcome. If you find a bug or would like to suggest a new feature, please create an issue in the GitHub repository. If you would like to contribute code, please fork the repository and create a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
