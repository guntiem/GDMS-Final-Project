import QtQuick
import QtQuick.Controls
import QtQml.Models
import Qt.labs.qmlmodels

Page {
    width: 850
    height: 480
    visible: true
    title: "Contacts screen page"

    Image {
        source: "/assets/bg.png"
        anchors.fill: parent
        fillMode: Image.PreserveAspectCrop
    }

    Text {
        text: "Contacts"
        font.pointSize: 16
        color: "white"
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: parent.top
        anchors.topMargin: 20
        visible: true
    }

    Button {
        anchors.left: parent.left
        anchors.bottom: parent.bottom
        anchors.margins: 50
        text: "Back"

        onClicked: {
            onClicked: pageLoader.source = ""
            buttonRow.visible = true
            console.log("Back to Main Menu")
        }
    }

    ListModel {
        id: contactsModel
        ListElement {name: "User"; phone: "123-456-7890"}
        ListElement {name: "User"; phone: "123-456-7890"}
        ListElement {name: "User"; phone: "123-456-7890"}
        ListElement {name: "User"; phone: "123-456-7890"}
        ListElement {name: "User"; phone: "123-456-7890"}
        ListElement {name: "User"; phone: "123-456-7890"}
        ListElement {name: "User"; phone: "123-456-7890"}
        ListElement {name: "User"; phone: "123-456-7890"}
        ListElement {name: "User"; phone: "123-456-7890"}
        ListElement {name: "User"; phone: "123-456-7890"}
        ListElement {name: "User"; phone: "123-456-7890"}
        ListElement {name: "User"; phone: "123-456-7890"}
        ListElement {name: "User"; phone: "123-456-7890"}
        ListElement {name: "User"; phone: "123-456-7890"}
        ListElement {name: "User"; phone: "123-456-7890"}
        ListElement {name: "User"; phone: "123-456-7890"}
        ListElement {name: "User"; phone: "123-456-7890"}
        ListElement {name: "User"; phone: "123-456-7890"}
        ListElement {name: "User"; phone: "123-456-7890"}
        ListElement {name: "User"; phone: "123-456-7890"}
        ListElement {name: "User"; phone: "123-456-7890"}
    }

    ScrollView {
        anchors.top: parent.top
        anchors.topMargin: 100
        anchors.bottom: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter
        width: parent.width * 0.8

        ListView {
            model: contactsModel

            delegate: Row {
                spacing: 20
                height: 40

                Text {
                    text: name
                    color: "white"
                    width: 250
                }

                Text {
                    text: phone
                    color: "white"
                    width: 200
                }
            }
        }
    }
}
