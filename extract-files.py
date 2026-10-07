#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

import re
from pathlib import Path

from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)


def lib_fixup_system_ext_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'system_ext' else None


lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'libSuperTextWrapper',
        'libXDocProcessSDK',
        'libYTCommon',
        'libextendfile',
        'libmpbase',
    ): lib_fixup_system_ext_suffix,
}

module = ExtractUtilsModule(
    'camera',
    'oplus',
    lib_fixups=lib_fixups,
    device_rel_path='vendor/oplus/camera',
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()

    # extract-utils turns dexpreopt off for every APK. OplusCamera is compiled
    # at build time (PRODUCT_DEXPREOPT_SPEED_APPS in opluscamera.mk).
    bp = Path(__file__).with_name('Android.bp')
    bp.write_text(
        re.sub(
            r'(name: "OplusCamera",.*?)    dex_preopt: \{\n        enabled: false,\n    \},\n',
            r'\1',
            bp.read_text(),
            count=1,
            flags=re.S,
        )
    )
