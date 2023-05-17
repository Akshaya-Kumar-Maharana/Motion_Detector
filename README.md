# Motion_Detector

This python script makes use of the inbuilt motion detector algorithm provided by OpenCV-MOG2 to detect any motion in the given frame. We can select the area to which we wish to apply the motion detector by using mouse clicks. Select the two corner points(top-left and bottom-right) on the main frame using mouse clicks. It detects the are where motion is detected and draws contours on the main video frame and gives a text indication of weather motion is detected or not.

# Dependencies
OpenCV-Python == 4.7.0

Numpy == 1.23.5

# Parametres

MOG2 takes in the following parameters:

'history': This parameter controls the number of previous frames that are used to build the background model. The higher the value of this parameter, the more adaptive the model will be to changes in the scene. The default value is 500.

'varThreshold': This parameter is used to control the threshold on the squared Mahalanobis distance between the pixel and the background model to decide whether a pixel belongs to the background or foreground. The default value is 16. 

'detectShadows': This parameter is a Boolean value that indicates whether to detect and mark shadows or not. If set to True, the algorithm will mark the shadow pixels as gray in the output mask. The default value is True.

'learningRate': The learning rate determines how quickly the background model is updated to adapt to changes in the scene. The default value is -1.

'shadowValue': This parameter sets the value that is used to mark the shadow pixels in the output mask. The default value is 127. 

'shadowThreshold':  This parameter controls the threshold used to detect shadows. It is the threshold on the ratio between the pixel and the corresponding background model component. If the ratio is below this threshold, the pixel is considered a shadow. The default value is 0.5.

'backgroundRatio': This parameter controls the ratio of the number of pixels in the background to the total number of pixels in the image. The default value is 0.9. 

'nmixtures':  This parameter controls the number of Gaussian distributions used to model the background. The default value is 5.
 
'fVarInit': This parameter sets the initial variance of each Gaussian component. The default value is 36. 

'fVarMin': This parameter sets the minimum variance of each Gaussian component. The default value is 4. 

'fVarMax':  This parameter sets the maximum variance of each Gaussian component. The default value is 75. 

'fCT': This parameter is the complexity reduction threshold. It controls when to remove a background model component. The default value is 0.05. 

'nShadowDetection': This parameter controls the number of frames to wait before re-enabling shadow detection after a shadow has been detected. The default value is 4. 

'fTau': This parameter is used to decide when to remove a Gaussian component. The default value is 0.5. 

'postprocess': This parameter is a Boolean value that indicates whether to apply post-processing to the output mask. If set to True, it will apply morphological operations to remove small objects and fill holes in the mask. The default value is True.

