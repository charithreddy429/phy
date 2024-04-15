import cv2


def get_out(filename: str, fps: int, size: (int, int)) -> object:
    """"
    use this to create a out
    add images to using out.write()
    finally use out.release() to save it
    """
    # Define the codec using VideoWriter_fourcc and create a VideoWriter object

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    out = cv2.VideoWriter(filename, fourcc, float(fps), size)

    return out