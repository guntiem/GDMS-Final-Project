import QtQuick
import QtQuick.Controls

Window {
    width: 850
    height: 480
    visible: true
    title: qsTr("GDMS Sample Application")

    Image {
        source: "/OCRtestingimages/bg.png"
        anchors.fill: parent
        fillMode: Image.PreserveAspectCrop
    }

    Item {
        //LayoutMirroring.enabled: true
        anchors.right: parent.right

        Row {
            anchors.fill: parent
            LayoutMirroring.enabled: true
            //layoutDirection: Qt.RightToLeft

            Image {
                id: alertIcon
                source: "/OCRtestingimages/alert.png"
                visible: alertIconEnable.checked
                width: 30
                height: 30
            }
            Image {
                id: headphoneIcon
                source: "/OCRtestingimages/headphones.png"
                visible: headphoneIconEnable.checked
                width: 30
                height: 30
            }
            Image {
                id: lockedIcon
                source: "/OCRtestingimages/locked.png"
                visible: lockedIconEnable.checked
                width: 30
                height: 30
            }
            Image {
                id: muteIcon
                source: "/OCRtestingimages/mute.png"
                visible: muteIconEnable.checked
                width: 30
                height: 30
            }
            Image {
                id: pauseIcon
                source: "/OCRtestingimages/pause.png"
                visible: pauseIconEnable.checked
                width: 30
                height: 30
            }
            Image {
                id: videoIcon
                source: "/OCRtestingimages/video.png"
                visible: videoIconEnable.checked
                width: 30
                height: 30
            }
            Image {
                id: voicemailIcon
                source: "/OCRtestingimages/voicemail.png"
                visible: voicemailIconEnable.checked
                width: 30
                height: 30
            }
        }
    }

    Item {
        anchors.fill: parent
        anchors.margins: 50

        Column {

            Text {
                text: "Icons to display:"
                font.pointSize: 14
                color: "white"
                // horizontalAlignment: Text.AlignHCenter
            }

            CheckBox {
                id: alertIconEnable
                text: "Alert"
                checked: false

                onCheckedChanged: {
                    if (checked) {
                        console.log("Alert icon displayed.")
                    } else {
                        console.log("Alert icon hidden.")
                    }
                }
            }

            CheckBox {
                id: headphoneIconEnable
                text: "Headphone"
                checked: false

                onCheckedChanged: {
                    if (checked) {
                        console.log("Headphone icon displayed.")
                    } else {
                        console.log("Headphone icon hidden.")
                    }
                }
            }

            CheckBox {
                id: lockedIconEnable
                text: "Locked"
                checked: false

                onCheckedChanged: {
                    if (checked) {
                        console.log("Locked icon displayed.")
                    } else {
                        console.log("Locked icon hidden.")
                    }
                }
            }

            CheckBox {
                id: muteIconEnable
                text: "Mute"
                checked: false

                onCheckedChanged: {
                    if (checked) {
                        console.log("Mute icon displayed.")
                    } else {
                        console.log("Mute icon hidden.")
                    }
                }
            }

            CheckBox {
                id: pauseIconEnable
                text: "Pause"
                checked: false

                onCheckedChanged: {
                    if (checked) {
                        console.log("Pause icon displayed.")
                    } else {
                        console.log("Pause icon hidden.")
                    }
                }
            }

            CheckBox {
                id: videoIconEnable
                text: "Video"
                checked: false

                onCheckedChanged: {
                    if (checked) {
                        console.log("Video icon displayed.")
                    } else {
                        console.log("Video icon hidden.")
                    }
                }
            }
            CheckBox {
                id: voicemailIconEnable
                text: "Voicemail"
                checked: false

                onCheckedChanged: {
                    if (checked) {
                        console.log("Voicemail icon displayed.")
                    } else {
                        console.log("Voicemail icon hidden.")
                    }
                }
            }
        }
    }
}
