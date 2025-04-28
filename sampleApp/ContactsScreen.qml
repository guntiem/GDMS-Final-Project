import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import Qt.labs.qmlmodels 1.0

Page {
    id: contactsTableView
    width: parent ? parent.width : 850
    height: parent ? parent.height : 480
    title: "Your Contacts"

    Image {
        source: "/assets/bg.png"
        anchors.fill: parent
        fillMode: Image.PreserveAspectCrop
    }

    TableModel {
        id: contactsModel
        objectName: "contactsModel"
        TableModelColumn { display: "First Name" }
        TableModelColumn { display: "Last Name" }
        TableModelColumn { display: "Phone" }
        TableModelColumn { display: "Email" }
        rows: [
            { "First Name": "Riv",  "Last Name": "Warrier",   "Phone": "123-456-7890", "Email": "john.doe@example.com" },
            { "First Name": "Mahir",  "Last Name": "Bose", "Phone": "234-567-8901", "Email": "jane.smith@example.com" },
            { "First Name": "Alice", "Last Name": "Jones", "Phone": "345-678-9012", "Email": "alice.jones@example.com" }
        ]
    }

    property var columnDefinitions: [
        { role: "First Name", title: "First Name", width: 150 },
        { role: "Last Name",  title: "Last Name",  width: 150 },
        { role: "Phone",      title: "Phone",      width: 150 },
        { role: "Email",      title: "Email",      width: 250 }
    ]

    Column {
        anchors.fill: parent
        spacing: 0

        Row {
            id: headerRow
            spacing: 0
            Repeater {
                model: columnDefinitions.length
                Rectangle {
                    width: columnDefinitions[index].width
                    height: 40
                    color: "#dddddd"
                    border.color: "black"
                    border.width: 1
                    Text {
                        anchors.centerIn: parent
                        text: columnDefinitions[index].title
                        font.bold: true
                    }
                }
            }
        }

        TableView {
            property int myColCount: 4
            id: tableView
            width: parent.width
            height: contactsTableView.height - headerRow.height
            model: contactsModel

            columnWidthProvider: function(column) {
                return columnDefinitions[column]
                       ? columnDefinitions[column].width
                       : 100;
            }

            delegate: Rectangle {
                implicitHeight: 40
                height: 40
                width: tableView.columnWidthProvider(column)
                border.width: 1
                border.color: "#cccccc"

                Text {
                    anchors.centerIn: parent
                    text: display
                }
            }
        }

        Text {
            id: firstEmailText
            objectName: "firstEmailText"
            visible: false
            text: contactsModel.rows[0].Email
        }
    }

    Button {
        id: backButton
        anchors.left: parent.left
        anchors.bottom: parent.bottom
        anchors.margins: 50
        text: "Back"
        onClicked: {
            pageLoader.source = ""
            buttonRow.visible = true
            console.log("Back to Main Menu")
        }
    }

    Button {
        id: addButton
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        anchors.margins: 50
        text: "New Contact"
        onClicked: addContactDialog.open()
    }

    Dialog {
        id: addContactDialog
        title: "Add New Contact"
        modal: true
        standardButtons: Dialog.Ok | Dialog.Cancel

        onAccepted: {
            // append the new row including email
            contactsModel.rows = contactsModel.rows.concat([{
                "First Name": firstNameField.text,
                "Last Name":  lastNameField.text,
                "Phone":      phoneField.text,
                "Email":      emailField.text
            }]);

            // clear inputs
            firstNameField.text = ""
            lastNameField.text  = ""
            phoneField.text     = ""
            emailField.text     = ""
        }

        contentItem: ColumnLayout {
            width: 300
            spacing: 10

            TextField {
                id: firstNameField
                placeholderText: "First Name"
                Layout.fillWidth: true
            }
            TextField {
                id: lastNameField
                placeholderText: "Last Name"
                Layout.fillWidth: true
            }
            TextField {
                id: phoneField
                placeholderText: "Phone"
                Layout.fillWidth: true
            }
            TextField {
                id: emailField
                placeholderText: "Email"
                Layout.fillWidth: true
            }
        }
    }
}
