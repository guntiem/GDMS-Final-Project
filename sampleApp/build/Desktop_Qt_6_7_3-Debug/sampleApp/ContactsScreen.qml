import QtQuick
import QtQuick.Controls

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

    Button {
        anchors.left: parent.left
        anchors.bottom: parent.bottom
        anchors.margins: 50
        text: "Back"

        onClicked: {
            onClicked: pageLoader.source = ""
            buttonRow.visible = true
            // onClicked: pageLoader.source = "Main.qml"
            console.log("Back to Main Menu")
        }
    }
}
