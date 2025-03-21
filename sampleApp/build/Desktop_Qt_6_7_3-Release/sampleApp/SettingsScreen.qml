/*import QtQuick
import QtQuick.Controls

Page {
    width: 850
    height: 480
    visible: true
    title: "Settings screen page"

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
}*/

import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Page {
    id: settingsPage
    width: 850
    height: 480
    visible: true
    title: "Settings Screen Page"
    property string currentThemeColor: "transparent"
    property int remainingAttempts: 3
    property bool securityLocked: false

    // Background Image (Always Visible)
    Image {
        source: "/assets/bg.png"
        anchors.fill: parent
        fillMode: Image.PreserveAspectCrop
    }

    // Theme Color Overlay (Semi-transparent)
    Rectangle {
        anchors.fill: parent
        color: currentThemeColor
        opacity: 0.6
        visible: currentThemeColor !== "transparent"
    }

    ScrollView {
        anchors.fill: parent
        contentWidth: parent.width
        clip: true

        Column {
            width: parent.width
            spacing: 15
            padding: 20

            Label {
                text: "Settings"
                font.bold: true
                font.pixelSize: 26
                color: "white"
            }

            // Volume Control
            Row {
                spacing: 10
                Label { text: "Volume"; color: "white"; font.pixelSize: 18 }
                Slider {
                    id: volumeSlider;
                    from: 0;
                    to: 100;
                    value: 50
                    onValueChanged: {
                        if (volumeSlider.value === 0) {
                            silentLabel.text = "Silent Mode";
                        } else if (volumeSlider.value === 100) {
                            silentLabel.text = "Full Volume";
                        }else {
                            silentLabel.text = "";
                        }
                    }

                }

                Label {
                    id: silentLabel
                    color: "white"
                    font.pixelSize: 18
                }
            }

            // Ring Volume (Vertical Slider)
            Row {
                spacing: 10
                Label { text: "Ring Volume"; color: "white"; font.pixelSize: 18 }
                Slider {
                    id: ringVolumeSlider;
                    from: 0;
                    to: 100;
                    value: 50
                    orientation: Qt.Vertical
                    height: 100
                    onValueChanged: {
                        if (volumeSlider.value === 0) {
                            silentLabel.text = "Silent Mode";
                        } else if (volumeSlider.value === 100) {
                            silentLabel.text = "Full Volume";
                        }else {
                            silentLabel.text = "";
                        }
                    }
                }
            }

            // Notification Volume (Vertical Slider)
            Row {
                spacing: 10
                Label { text: "Notification Volume"; color: "white"; font.pixelSize: 18 }
                Slider {
                    id: notificationVolumeSlider;
                    from: 0;
                    to: 100;
                    value: 50
                    orientation: Qt.Vertical
                    height: 100
                    onValueChanged: {
                        if (volumeSlider.value === 0) {
                            silentLabel.text = "Silent Mode";
                        } else if (volumeSlider.value === 100) {
                            silentLabel.text = "Full Volume";
                        }else {
                            silentLabel.text = "";
                        }
                    }
                }
            }

            // Language Selection
            Row {
                spacing: 10
                Label { text: "Language"; color: "white"; font.pixelSize: 18 }
                ComboBox {
                    id: languageSelector
                    model: ["English", "Spanish", "German"]
                    font.pixelSize: 16
                    onActivated: {
                        switch (currentIndex) {
                            case 0: console.log("Language changed to English"); break;
                            case 1: console.log("Idioma cambiado a Español"); break;
                            case 2: console.log("Sprache zu Deutsch geändert"); break;
                        }
                    }
                }
            }

            // Security Settings (Long Press to Open)
            Button {
                text: "Security Settings"
                font.pixelSize: 18

                MouseArea {
                    anchors.fill: parent
                    onPressed: pressAndHoldTimer.start()
                    onReleased: pressAndHoldTimer.stop()

                    Timer {
                        id: pressAndHoldTimer
                        interval: 1000
                        repeat: false
                        onTriggered: {
                            if (!securityLocked) securityPopup.open()
                            else console.log("Security locked. Try again later.")
                        }
                    }
                }
            }

            // Theme Selection (One Click)
            Row {
                spacing: 10
                Label { text: "Mode"; color: "white"; font.pixelSize: 18 }
                ComboBox {
                    id: themeSelector
                    model: ["Light", "Dark"]
                    font.pixelSize: 16
                    onActivated: console.log("Mode changed to: " + themeSelector.currentText)
                }
            }

            // Theme Preview (Double Click to Apply)
            Label { text: "Theme Preview"; color: "white"; font.pixelSize: 18 }

            ScrollView {
                width: parent.width
                height: 80
                contentWidth: themeRow.width
                clip: true

                Row {
                    id: themeRow
                    spacing: 15

                    Repeater {
                        model: ["Blue", "Green", "Pink", "Beige"]
                        delegate: Rectangle {
                            width: 100
                            height: 60
                            color: modelData.toLowerCase()
                            border.color: "white"

                            Text {
                                anchors.centerIn: parent
                                text: modelData
                                font.pixelSize: 16
                                color: "black"
                            }

                            MouseArea {
                                anchors.fill: parent
                                onDoubleClicked: {
                                    settingsPage.currentThemeColor = modelData.toLowerCase()
                                    console.log("Background overlay changed to: " + modelData)
                                }
                            }
                        }
                    }
                }
            }

            // Back Button
            Button {
                anchors.horizontalCenter: parent.horizontalCenter
                text: "Back"
                font.pixelSize: 18
                onClicked: {
                    pageLoader.source = ""
                    buttonRow.visible = true
                    console.log("Back to Main Menu")
                }
            }
        }
    }

    // Security Popup
    Popup {
        id: securityPopup
        width: 300
        height: 200
        modal: true
        closePolicy: Popup.CloseOnEscape
        background: Rectangle { color: "white"; radius: 10 }

        anchors.centerIn: parent

        Column {
            anchors.centerIn: parent
            spacing: 10

            Label {
                text: "Enter Password:"
                font.pixelSize: 18
                anchors.horizontalCenter: parent.horizontalCenter
            }

            TextField {
                id: passwordField
                width: 200
                echoMode: TextInput.Password
                font.pixelSize: 18
                anchors.horizontalCenter: parent.horizontalCenter
            }

            Button {
                text: "Submit"
                font.pixelSize: 16
                anchors.horizontalCenter: parent.horizontalCenter
                onClicked: {
                    if (passwordField.text === "1234") {
                        console.log("Access Granted")
                        securityPopup.close()
                        securitySettingsPopup.open()
                    } else {
                        settingsPage.remainingAttempts--
                        if (settingsPage.remainingAttempts > 0) {
                            wrongPasswordLabel.text = "Incorrect password. " + settingsPage.remainingAttempts + " attempts left.";
                        } else {
                            wrongPasswordLabel.text = "Too many failed attempts. Try again in 90 seconds.";
                            securityLocked = true
                        }
                    }
                }
            }

            Button {
                text: "Close"
                font.pixelSize: 16
                anchors.horizontalCenter: parent.horizontalCenter
                onClicked: securityPopup.close()
            }


            Label {
                id: wrongPasswordLabel
                color: "red"
                font.pixelSize: 16
                anchors.horizontalCenter: parent.horizontalCenter
            }
        }
    }

    // Security Settings Popup
    Popup {
        id: securitySettingsPopup
        width: 300
        height: 250
        modal: true
        closePolicy: Popup.CloseOnEscape
        background: Rectangle { color: "white"; radius: 10 }

        Column {
            anchors.centerIn: parent
            spacing: 10

            Label {
                text: "Security Settings"
                font.pixelSize: 20
                font.bold: true
                anchors.horizontalCenter: parent.horizontalCenter
            }

            Button {
                text: "Change Password"
                font.pixelSize: 16
                anchors.horizontalCenter: parent.horizontalCenter
                onClicked: console.log("Change Password Clicked")
            }

            Button {
                text: "Delete History"
                font.pixelSize: 16
                anchors.horizontalCenter: parent.horizontalCenter
                onClicked: console.log("Delete History Clicked")
            }

            Button {
                text: "Close"
                font.pixelSize: 16
                anchors.horizontalCenter: parent.horizontalCenter
                onClicked: securitySettingsPopup.close()
            }
        }
    }

    // Security Lock Timer
    Timer {
        id: securityTimer
        interval: 90000  // 90 seconds
        repeat: false
        onTriggered: {
            securityLocked = false
            settingsPage.remainingAttempts = 3
            console.log("Security unlocked. You can try again.")
        }
        running: securityLocked
    }
}

