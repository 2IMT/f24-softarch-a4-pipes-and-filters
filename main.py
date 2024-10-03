import cv2
from video_source import VideoSource
from filters.black_and_white import BlackAndWhiteFilter
from filters.mirror import MirrorFilter
from filters.resize import ResizeFilter
from filters.edge_detection import EdgeDetectionFilter


def stack_frames(frames):
    top_row = cv2.hconcat([frames[0], frames[1]])
    bottom_row = cv2.hconcat([frames[2], frames[3]])
    result = cv2.vconcat([top_row, bottom_row])
    return result


def main():
    source = VideoSource(0)

    filters = [
        BlackAndWhiteFilter(),
        MirrorFilter(),
        ResizeFilter(),
        EdgeDetectionFilter()
    ]

    while True:
        frame = source.get_frame()
        if frame is None:
            break

        processed_frames = [filter.apply(frame) for filter in filters]

        for i in range(len(processed_frames)):
            if len(processed_frames[i].shape) == 2:
                processed_frames[i] = cv2.cvtColor(
                    processed_frames[i], cv2.COLOR_GRAY2BGR)
            processed_frames[i] = cv2.resize(processed_frames[i], (320, 240))

        combined_frame = stack_frames(processed_frames)

        cv2.imshow("Processed Frames", combined_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    source.release()


if __name__ == "__main__":
    main()
