
import run_depth 
model_name = 'mono+stereo_640x192'
output_directory = '../depthEstimate'
no_cuda = True
# object2vec = False
run_depth.test_simple(model_name,output_directory,no_cuda)