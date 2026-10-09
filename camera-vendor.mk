#
# Automatically generated file. DO NOT MODIFY
#

PRODUCT_SOONG_NAMESPACES += \
    vendor/oplus/camera

PRODUCT_COPY_FILES += \
    vendor/oplus/camera/proprietary/odm/etc/camera/license_release_fdc.lic:$(TARGET_COPY_OUT_ODM)/etc/camera/license_release_fdc.lic \
    vendor/oplus/camera/proprietary/odm/etc/camera/model/license.lic:$(TARGET_COPY_OUT_ODM)/etc/camera/model/license.lic \
    vendor/oplus/camera/proprietary/odm/etc/camera/singleblur/license_release.lic:$(TARGET_COPY_OUT_ODM)/etc/camera/singleblur/license_release.lic \
    vendor/oplus/camera/proprietary/odm/etc/camera/singleblur/license_release.license:$(TARGET_COPY_OUT_ODM)/etc/camera/singleblur/license_release.license

PRODUCT_PACKAGES += \
    libpenguin \
    libHeifEncoderWrapper \
    libNativeWinBuffExchange \
    liboplusheifwriter \
    OplusAppPlatform \
    oplus-support-wrapper
