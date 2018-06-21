import sys
sys.path.append('/workspace/mnt/group/face-det/zhubin/caffe/python')
import caffe
caffe.set_device(0)
caffe.set_mode_gpu()
solver = caffe.SGDSolver('/workspace/mnt/group/face-det/zhubin/Face_attr_recognition/solver.prototxt')
solver.solve()
