import QtQuick
import QtQuick.Controls

Window {
    width: 850
    height: 480
    visible: true
    title: qsTr("GDMS Sample Application")

    Image {
        source: "assets/mainBg.png"
        anchors.fill: parent
        fillMode: Image.PreserveAspectCrop
    }

    Item {
        id: pageButtons
        width: 1440
        height: 800

        Loader { id: pageLoader }

        Rectangle {
            id: clickableArea
            width: 50
            height: 50
            color: "transparent"
            anchors.centerIn: parent


            MouseArea {
                anchors.fill: parent
                onClicked: {
                    onClicked: pageLoader.source = "OCRMenuTesting.qml"
                    console.log("OCR Testing Page Loaded.")
                }
            }
        }
    }
}
