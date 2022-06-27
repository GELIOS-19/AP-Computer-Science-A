import React, { useRef, useState } from "react";
import {
  StyleSheet,
  View,
  PanResponder,
  GestureResponderEvent,
  PanResponderGestureState,
  Animated,
  LayoutRectangle,
} from "react-native";
import Svg, { G, Path } from "react-native-svg";

interface PaintCanvasProps {
  width: number;
  height: number;
  color: string;
  strokeSize: number;
}

const PaintCanvas = (props: PaintCanvasProps): JSX.Element => {
  const [points, setPoints] = useState<{ x: number, y: number }[]>([]);
  const [paths, setPaths] = useState<JSX.Element[]>([]);

  const pointsToSvgPathConverter = new _PointsToSvgPathConverter();
  
  const panResponder = useRef(
    PanResponder.create({
      onStartShouldSetPanResponder: (
        e: GestureResponderEvent,
        gestureState: PanResponderGestureState
      ) => true,
      onMoveShouldSetPanResponder: (
        e: GestureResponderEvent,
        gestureState: PanResponderGestureState
      ) => true,
      onPanResponderGrant: (
        e: GestureResponderEvent,
        gestureState: PanResponderGestureState
      ) => {
        const [x, y] = [e.nativeEvent.pageX, e.nativeEvent.pageY];
        const newPoints = points;
        newPoints.push({ x, y });
        setPoints(newPoints);
      },
      onPanResponderMove: (
        e: GestureResponderEvent,
        gestureState: PanResponderGestureState
      ) => {
        const [x, y] = [e.nativeEvent.pageX, e.nativeEvent.pageY];
        const newPoints = points;
        newPoints.push({ x, y });
        setPoints(newPoints);
      },
      onPanResponderRelease: (
        e: GestureResponderEvent,
        gestureState: PanResponderGestureState
      ) => {
        const newPaths = paths;
        if (points.length > 0) {
          newPaths.push(
            <Path
              d={pointsToSvgPathConverter.pointsToSvgPath(points)}
              stroke={props.color}
              strokeWidth={props.strokeSize}
              fill="none"
            />
          );
        }
        setPoints([]);
        setPaths(paths);
      },
    })
  ).current;

  return (
    <View
      onLayout={(e) =>
        pointsToSvgPathConverter.setOffsets(e.nativeEvent.layout)
      }
      style={styles.paintContainer}
    >
      <Animated.View {...panResponder.panHandlers}>
        <Svg
          style={styles.paintSurface}
          width={props.width}
          height={props.height}
        >
          <G>{paths}</G>
        </Svg>
      </Animated.View>
    </View>
  );
};

const styles = StyleSheet.create({
  paintContainer: {
    borderWidth: 0.5,
    borderColor: "#DDDDDD",
  },

  paintSurface: {
    backgroundColor: "transparent",
  },
});

class _PointsToSvgPathConverter {
  _offsetX: number = 0;
  _offsetY: number = 0;

  setOffsets(layout: LayoutRectangle): void {
    this._offsetX = layout.x;
    this._offsetY = layout.y;
  }

  pointsToSvgPath(points: { x: number; y: number }[]): string {
    if (points.length > 0) {
      let path = `M ${points[0].x - this._offsetX} ${points[0].y - this._offsetY} `;
      points.forEach((point: { x: number; y: number }) => {
        path = `${path} L ${point.x - this._offsetX} ${point.y - this._offsetY} `;
      });
      return path;
    } else {
      return "";
    }
  }
}

export default PaintCanvas;