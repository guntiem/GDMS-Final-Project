import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Page {
    width: 850
    height: 480
    visible: true
    title: "Lock screen page"

    Image {
        source: "/assets/bg.png"
        anchors.fill: parent
        fillMode: Image.PreserveAspectCrop
    }

    Text {
        text: "Screen is locked."
        font.pointSize: 16
        color: "white"
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: parent.top
        anchors.topMargin: 20
        visible: true
    }

    Column {
        spacing: 10
        anchors.centerIn: parent

        TextField {
            id: passwordField
            width: 250
            height: 50
            font.pointSize: 24
            color: "black"
            background: Rectangle {
                color: "white"
                radius: 10
            }
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
        }

        Button {
            id: checkPasswordButton
            anchors.horizontalCenter: parent.horizontalCenter
            text: qsTr("Unlock Phone")
            onClicked: {
                if (passwordField.text === "1234") {
                    pageLoader.source = ""
                    buttonRow.visible = true
                } else {
                    console.log("User entered incorrect password.")
                    passwordField.text = ""
                }
            }
        }
    }
}
