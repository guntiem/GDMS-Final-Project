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
        anchors.leftMargin: parent.width * 1/9
        anchors.bottomMargin: parent.height * 1/9
        width: parent.width * 1/15
        height: parent.height * 1/30
        text: "Back"

        onClicked: {
            onClicked: pageLoader.source = ""
            buttonRow.visible = true
            console.log("Back to Main Menu")
        }
    }

    ListModel {
        id: numberPadModel
        ListElement { primaryText: "1"; secondaryText: "" }
        ListElement { primaryText: "2"; secondaryText: "ABC" }
        ListElement { primaryText: "3"; secondaryText: "DEF" }
        ListElement { primaryText: "4"; secondaryText: "GHI" }
        ListElement { primaryText: "5"; secondaryText: "JKL" }
        ListElement { primaryText: "6"; secondaryText: "MNO" }
        ListElement { primaryText: "7"; secondaryText: "PQRS" }
        ListElement { primaryText: "8"; secondaryText: "TUV" }
        ListElement { primaryText: "9"; secondaryText: "WXYZ" }
        ListElement { primaryText: "*"; secondaryText: "" }
        ListElement { primaryText: "0"; secondaryText: "+" }
        ListElement { primaryText: "#"; secondaryText: "" }
    }

    Rectangle {
        anchors.centerIn: parent
        width: parent.width * 4/5; height: parent.height * 2/3;
        color: "gray"

        Row {
            anchors.fill: parent

            Rectangle {
                width: parent.width * 1/5; height: parent.height;

                Column {
                    anchors.fill: parent

                    Rectangle {
                        width: parent.width; height: parent.height * 1/2

                        TextField {
                            id: phoneNumberField
                            width: parent.width * 5/6; height: parent.height * 1/5
                            anchors.top: parent.top
                            anchors.left: parent.left;
                            readOnly: true
                        }
                        Button {
                            id: backspaceButton
                            width: parent.width * 1/6; height: parent.height * 1/5
                            anchors.top: parent.top
                            anchors.right: parent.right
                            text: "<"
                            onClicked: {
                                let s = phoneNumberField.text;
                                phoneNumberField.text = s.slice(0, -1);
                            }
                        }
                    }

                    GridView {
                        id: numberPad
                        width: parent.width; height: parent.height * 4/10
                        cellWidth: width * 1/3; cellHeight: height * 1/4
                        interactive: false
                        model: numberPadModel

                        delegate: Button {
                            width: numberPad.cellWidth; height: numberPad.cellHeight
                            text: primaryText + "\n" + secondaryText
                            onClicked: {
                               phoneNumberField.text += primaryText;
                            }
                        }
                    }

                    Button {
                        id: callButton
                        width: parent.width; height: parent.height * 1/10
                        text: "Call"
                        onClicked: {
                            phoneModel.insert(0, {name: "John Doe", number: phoneNumberField.text});
                            phoneNumberField.text = "";
                        }
                    }
                }
            }

            ListModel {
                id: phoneModel
                ListElement{ name: "John Doe"; number: "111-111-1111"}
                ListElement{ name: "John Doe"; number: "222-222-2222"}
                ListElement{ name: "John Doe"; number: "333-333-3333"}
                ListElement{ name: "John Doe"; number: "444-444-4444"}
                ListElement{ name: "John Doe"; number: "555-555-5555"}
                ListElement{ name: "John Doe"; number: "666-666-6666"}
                ListElement{ name: "John Doe"; number: "777-777-7777"}
                ListElement{ name: "John Doe"; number: "888-888-8888"}
                ListElement{ name: "John Doe"; number: "999-999-9999"}
                ListElement{ name: "John Doe"; number: "000-000-0000"}
            }

            ListView {
                id: phoneView
                width: parent.width * 4/5; height: parent.height
                spacing: 2
                clip: true
                model: phoneModel
                delegate: Rectangle {
                    id: phoneDelegate
                    width: phoneView.width; height: 75;
                    property int callDuration: 0
                    property string button1Text: "Answer"

                    Rectangle {
                        id: innerRect
                        width: phoneDelegate.width * 2/3; height: phoneDelegate.height;
                        color: "slategray"
                        anchors.left: phoneDelegate.left
                        anchors.right: answerButton.left

                        /*MouseArea {
                            anchors.fill: parent
                            hoverEnabled: true
                            onEntered: {
                                parent.color = "lightgray";
                            }
                            onExited: {
                                parent.color = "slategray";
                            }
                        }*/

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
                        text: button1Text
                        display: "TextUnderIcon"
                        width: phoneDelegate.width * 1/9; height: phoneDelegate.height
                        anchors.right: endButton.left
                        onClicked: {
                            if (text === "Answer") {
                                text = "Hold";
                                callTimer.start();
                            }
                            else if (text === "Hold") {
                                text = "Resume";
                                callTimer.stop();
                            }
                            else if (text === "Resume") {
                                text = "Hold";
                                callTimer.start();
                            }
                        }
                    }

                    Button {
                        id: endButton
                        icon.source: "/assets/call_button.png"
                        text: qsTr("End")
                        display: "TextUnderIcon"
                        width: phoneDelegate.width * 1/9; height: phoneDelegate.height
                        anchors.right: mergeButton.left
                        onClicked: {
                            phoneModel.remove(index);
                        }
                    }

                    Button {
                        id: mergeButton
                        icon.source: "/assets/call_button.png"
                        text: qsTr("Merge")
                        display: "TextUnderIcon"
                        width: phoneDelegate.width * 1/9; height: phoneDelegate.height
                        anchors.right: phoneDelegate.right
                    }

                    Item {
                        Timer {
                            id: callTimer
                            interval: 1000; running: false; repeat: true
                            onTriggered: {
                                callDuration++;
                                phoneTime.text =
                                    Math.floor(callDuration / 60).toString().padStart(2, "0") +
                                    ":" +
                                    (callDuration % 60).toString().padStart(2, "0");
                            }
                        }
                    }
                }
            }
        }
    }

    component FillerButton : Button {
        icon.source: "/assets/settings_button.png"
        text: qsTr("Button")
        display: "TextUnderIcon"
        Layout.fillHeight: true
        Layout.fillWidth: true
    }

    RowLayout {
        id: bottomControlBar
        height: parent.height / 10
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
