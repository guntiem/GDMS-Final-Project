import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Page {
    width: 850
    height: 480
    visible: true
    title: "Phone screen page"

    Image {
        source: "/assets/bg.png"
        anchors.fill: parent
        fillMode: Image.PreserveAspectCrop
    }

    Button {
        anchors.left: parent.left
        anchors.bottom: parent.bottom
        anchors.margins: 100
        text: "Back"

        onClicked: {
            onClicked: pageLoader.source = ""
            buttonRow.visible = true
            // onClicked: pageLoader.source = "Main.qml"
            console.log("Back to Main Menu")
        }
    }

    Rectangle {
        anchors.centerIn: parent
        width: parent.width * 4/5; height: parent.height * 1/2;
        color: "transparent"

        ListModel {
            id: phoneModel
            ListElement{ name: "Jane Doe"; number: "555-555-5555"}
            ListElement{ name: "Jane Doe"; number: "555-555-5555"}
            ListElement{ name: "Jane Doe"; number: "555-555-5555"}
            ListElement{ name: "Jane Doe"; number: "555-555-5555"}
            ListElement{ name: "Jane Doe"; number: "555-555-5555"}
            ListElement{ name: "Jane Doe"; number: "555-555-5555"}
            ListElement{ name: "Jane Doe"; number: "555-555-5555"}
            ListElement{ name: "Jane Doe"; number: "555-555-5555"}
            ListElement{ name: "Jane Doe"; number: "555-555-5555"}
            ListElement{ name: "Jane Doe"; number: "555-555-5555"}
            ListElement{ name: "Jane Doe"; number: "555-555-5555"}
        }

        ListView {
            id: phoneView
            anchors.fill: parent
            spacing: 5

            model: phoneModel
            delegate: Rectangle {
                id: phoneDelegate
                width: phoneView.width; height: 75;

                Rectangle {
                    width: phoneDelegate.width * 2/3; height: phoneDelegate.height;
                    color: "slategray"
                    anchors.left: phoneDelegate.left
                    anchors.right: answerButton.left

                    MouseArea {
                        anchors.fill: parent
                        hoverEnabled: true
                        onEntered: {
                            parent.color = "lightgray";
                        }
                        onExited: {
                            parent.color = "slategray";
                        }
                    }

                    Image {
                        id: phoneIcon
                        source: "/assets/call_button.png"
                        width: parent.height * 1/2; height: width
                        anchors.top: parent.top
                        anchors.horizontalCenter: parent.left
                        anchors.horizontalCenterOffset: width
                    }

                    Text {
                        id: phoneIconText
                        text: qsTr("FOO")
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.verticalCenterOffset: parent.height * 1/4
                        anchors.horizontalCenter: phoneIcon.horizontalCenter
                    }

                    Text {
                        id: phoneName
                        text: name
                        font.pointSize: 20
                        anchors.verticalCenter: phoneIcon.verticalCenter
                        anchors.left: parent.left
                        anchors.leftMargin: parent.height
                    }

                    Text {
                        id: phoneNumber
                        text: number
                        font.pointSize: 20
                        anchors.verticalCenter: phoneIconText.verticalCenter
                        anchors.left: parent.left
                        anchors.leftMargin: parent.height
                    }

                    Text {
                        id: phoneTime
                        text: qsTr("00:00")
                        font.pointSize: 12.5
                        anchors.top: parent.top
                        anchors.topMargin: 5
                        anchors.right: parent.right
                        anchors.rightMargin: 5
                    }
                }

                Button {
                    id: answerButton
                    icon.source: "/assets/call_button.png"
                    text: qsTr("Answer")
                    display: "TextUnderIcon"
                    width: phoneDelegate.width * 1/9; height: phoneDelegate.height
                    anchors.right: endButton.left
                }

                Button {
                    id: endButton
                    icon.source: "/assets/call_button.png"
                    text: qsTr("End")
                    display: "TextUnderIcon"
                    width: phoneDelegate.width * 1/9; height: phoneDelegate.height
                    anchors.right: mergeButton.left
                }

                Button {
                    id: mergeButton
                    icon.source: "/assets/call_button.png"
                    text: qsTr("Merge")
                    display: "TextUnderIcon"
                    width: phoneDelegate.width * 1/9; height: phoneDelegate.height
                    anchors.right: phoneDelegate.right
                }
            }
        }
    }

    component FillerButton : Button {
        icon.source: "/assets/settings_button.png"
        text: qsTr("Button")
        display: "TextUnderIcon"
        Layout.fillHeight: true
    }

    RowLayout {
        id: bottomControlBar
        height: 75
        anchors.bottom: parent.bottom
        anchors.left: parent.left
        anchors.right: parent.right
        spacing: 0

        FillerButton{}FillerButton{}FillerButton{}FillerButton{}FillerButton{}
        FillerButton{}FillerButton{}FillerButton{}FillerButton{}FillerButton{}
        FillerButton{}FillerButton{}FillerButton{}FillerButton{}FillerButton{}
        FillerButton{}FillerButton{}FillerButton{}FillerButton{}
    }
}

