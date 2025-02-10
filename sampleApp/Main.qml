import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 850
    height: 480
    visible: true
    title: qsTr("GDMS Sample Application")

    Image {
        source: "/assets/bg.png"
        anchors.fill: parent
        fillMode: Image.PreserveAspectCrop
    }

    Loader {
        id: pageLoader
        anchors.fill: parent
    }

    Text {
        text: "Home"
        font.pointSize: 16
        color: "white"
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: parent.top
        anchors.topMargin: 20
        visible: pageLoader.source == ""
    }

    Column {
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
        spacing: 10
        visible: pageLoader.source == ""

        Text {
            id: currentTime
            font.pointSize: 54
            color: "white"
            horizontalAlignment: Text.AlignHCenter
            text: Qt.formatDateTime(new Date(), "hh:mm")
        }

        Text {
            id: currentDate
            font.pointSize: 30
            color: "white"
            horizontalAlignment: Text.AlignHCenter
            text: Qt.formatDateTime(new Date(), "dd MMMM yyyy")
        }

        Timer {
            interval: 1000
            running: true
            repeat: true
            onTriggered: {
                var now = new Date();
                currentTime.text = Qt.formatDateTime(now, "hh:mm")
                currentDate.text = Qt.formatDateTime(now, "dd MMMM yyyy")
            }
        }
    }

    RowLayout {

        id: buttonRow

        height: 100

        anchors {
            horizontalCenter: parent.horizontalCenter
            top: parent.top
            topMargin: 360
        }
        spacing: 25

        // Lock button
        RoundButton {
            text: ""
            display: AbstractButton.IconOnly

            Layout.preferredWidth: 85
            Layout.preferredHeight: 85

            background: Image {
                anchors.fill: parent
                source: "/assets/lock_screen_button.png"
                fillMode: Image.PreserveAspectFit
            }

            radius: width / 2

            onClicked: {
                pageLoader.source = "LockScreen.qml"
                buttonRow.visible = false
                console.log("Lock Screen Page Loaded.")
            }
        }

        // Contacts button
        RoundButton {
            text: ""
            display: AbstractButton.IconOnly

            Layout.preferredWidth: 85
            Layout.preferredHeight: 85

            background: Image {
                anchors.fill: parent
                source: "/assets/contact_screen_button.png"
                fillMode: Image.PreserveAspectFit
            }

            radius: width / 2

            onClicked: {
                pageLoader.source = "ContactsScreen.qml"
                buttonRow.visible = false
                console.log("Contacts Page Loaded.")
            }
        }

        // Call history button
        RoundButton {
            text: ""
            display: AbstractButton.IconOnly

            Layout.preferredWidth: 85
            Layout.preferredHeight: 85

            background: Image {
                anchors.fill: parent
                source: "/assets/call_history_screen_button.png"
                fillMode: Image.PreserveAspectFit
            }

            radius: width / 2

            onClicked: {
                pageLoader.source = "HistoryScreen.qml"
                buttonRow.visible = false
                console.log("Call History Page Loaded.")
            }
        }

        // Call button
        RoundButton {
            text: ""
            display: AbstractButton.IconOnly

            Layout.preferredWidth: 85
            Layout.preferredHeight: 85

            background: Image {
                anchors.fill: parent
                source: "/assets/call_button.png"
                fillMode: Image.PreserveAspectFit
            }

            radius: width / 2

            onClicked: {
                pageLoader.source = "PhoneScreen.qml"
                buttonRow.visible = false
                console.log("Call Page Loaded.")
            }
        }

        // Settings button
        RoundButton {
            text: ""
            display: AbstractButton.IconOnly

            Layout.preferredWidth: 85
            Layout.preferredHeight: 85

            background: Image {
                anchors.fill: parent
                source: "/assets/settings_button.png"
                fillMode: Image.PreserveAspectFit
            }

            radius: width / 2

            onClicked: {
                pageLoader.source = "SettingsScreen.qml"
                buttonRow.visible = false
                console.log("Settings Page Loaded.")
            }
        }

        // Info button
        RoundButton {
            text: ""
            display: AbstractButton.IconOnly

            Layout.preferredWidth: 85
            Layout.preferredHeight: 85

            background: Image {
                anchors.fill: parent
                source: "/assets/info_screen_button.png"
                fillMode: Image.PreserveAspectFit
            }

            radius: width / 2

            onClicked: {
                pageLoader.source = "OCRMenuTesting.qml"
                buttonRow.visible = false
                console.log("Page Loaded.")
            }
        }

    }

}
