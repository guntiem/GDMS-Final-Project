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

    // Incorrect password modal pop up
    Dialog {
        id: incorrectPassDialog
        modal: true
        visible: false
        standardButtons: Dialog.Ok
        anchors.centerIn: parent

        contentItem: Column {
            spacing: 10
            padding: 20

            Text {
                objectName: "incorrectPassEnteredText"
                text: "Incorrect password."
            }
        }
    }

    // Correct password modal pop up, also return to home screen
    Dialog {
        id: correctPassDialog
        modal: true
        visible: false
        standardButtons: Dialog.Ok
        anchors.centerIn: parent

        onAccepted: {
            pageLoader.source = ""
            buttonRow.visible = true
        }

        contentItem: Column {
            spacing: 10
            padding: 20

            Text {
                objectName: "correctPassEnteredText"
                text: "Correct password entered, returning to home."
            }
        }
    }

    // Added this bool flag for navigating back to the home page depending on whether the entered password is correct or not
    property bool correctPassword: false

    Timer {
        id: modalTimer
        interval: 5000
        repeat: false
        onTriggered: {
            correctPassDialog.close()
            incorrectPassDialog.close()

            if (correctPassword) {
                pageLoader.source = ""
                buttonRow.visible = true
            }
        }
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
                    correctPassword = true
                    correctPassDialog.open()
                    modalTimer.restart()
                } else {
                    console.log("User entered incorrect password.")
                    correctPassword = false
                    passwordField.text = ""

                    incorrectPassDialog.open()
                    modalTimer.restart()
                }
            }
        }
    }
}
