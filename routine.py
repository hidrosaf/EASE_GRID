import h5py
import gdal, gdalconst
import numpy
from osgeo import osr

# file_ = "data.h5"
# dataset_ = "dataset_1"
# f = h5py.File(file_, 'r')
# d_set = f[dataset_]
#
# transformation_matrix = {
#     # "H13":      [(-25.12500, 0.25, 0.0, 75.125, 0.0, -0.25), (201, 281), [75.000, -25.000], [25.000, 45.0000]],
#     "EASE":   [(-180.12500, 0.25, 0.0, 90.125, 0.0, -0.25), (586, 1383), [90.000, -180.000], [-90.000, 180.0000]],
#     "GLOBAL":   [(-180.12500, 0.25, 0.0, 90.125, 0.0, -0.25), (721, 1441), [90.000, -180.000], [-90.000, 180.0000]],
# }
#
#
#
# source = osr.SpatialReference()
# source.ImportFromEPSG(6933)
#
# target = osr.SpatialReference()
# target.ImportFromEPSG(4326)
#
#
# src_filename = 'EASE_2.tif'
# src = gdal.Open(src_filename, gdalconst.GA_ReadOnly)
# src_proj = src.GetProjection()
# src_geotrans = src.GetGeoTransform()
#
# transform = osr.CoordinateTransformation(source, target)
#
# counter =4
# # input_data = gdal.GetDriverByName("GTiff").Create("EASE_%d.tif" %counter, transformation_matrix['EASE'][1][1], transformation_matrix['EASE'][1][0], 1, gdal.GDT_Float32)
# # input_data.GetRasterBand(1).WriteArray(numpy.array(d_set)*1000)
# # input_data.SetGeoTransform(transformation_matrix['EASE'][0])
#
# # input_data.SetProjection(source.ExportToWkt())
#
# export_data = gdal.GetDriverByName("GTiff").Create("z_%d.tif" %counter, transformation_matrix['GLOBAL'][1][1], transformation_matrix['GLOBAL'][1][0], 1, gdal.GDT_Float32)
# export_data.SetGeoTransform(transformation_matrix['GLOBAL'][0])
# export_data.SetProjection(target.ExportToWkt())
# export_data.FlushCache()
# gdal.ReprojectImage(src, export_data, src_proj, target.ExportToWkt(), gdalconst.GRA_NearestNeighbour)
# # input_data.FlushCache()
#
# print(d_set)
# f.close()


#
# import numpy
#
# lats = numpy.fromfile('EASE2_M25km.lats.1388x584x1.double',
#                       dtype=numpy.float64).reshape((584, 1386))
# lons = numpy.fromfile('EASE2_M25km.lons.1388x584x1.double',
#                       dtype=numpy.float64).reshape((584, 1386))
#
#
#
# from ease_grid import EASE2_grid
# egrid = EASE2_grid(25000)
# assert egrid.shape == (586, 1383)
# # these two attributes contain the longitude and latitude coordinate dimension
# egrid.londim
# egrid.latdim
#
#
# file_ = "data.h5"
# dataset_ = "dataset_1"
# f = h5py.File(file_, 'r')
# d_set = f[dataset_]
# c = numpy.array(d_set).transpose().ravel()
#
# k = 0
# with open("z_3.csv", "w") as f:
#     for i in egrid.londim:
#         for j in egrid.latdim:
#             f.write("%lf ;; %lf\t %lf\t\n" % (i, j, c[k]))
#             k += 1
#
# print "a"
#

from netCDF4 import Dataset
import os
path_ = "C:\Users\HPZ640\Downloads"
fr = Dataset(os.path.join(path_, 'air.mon.mean.nc'))
air = fr.variables['air'][0,:,:]
lat = fr.variables['lat'][:]
lon = fr.variables['lon'][:]
fr.close()

from ease_grid import EASE2_grid
egrid = EASE2_grid(25000)
assert egrid.shape == (586, 1383)
# these two attributes contain the longitude and latitude coordinate dimension
egrid.londim
egrid.latdim



import numpy

lats = numpy.fromfile('EASE2_M25km.lats.1388x584x1.double',
                      dtype=numpy.float64).reshape((584, 1386))
lons = numpy.fromfile('EASE2_M25km.lons.1388x584x1.double',
                      dtype=numpy.float64).reshape((584, 1386))


import pyresample


file_ = "data.h5"
dataset_ = "dataset_1"
f = h5py.File(file_, 'r')
d_set = f[dataset_]
c = numpy.array(d_set).transpose().ravel()
