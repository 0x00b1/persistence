import pytest


def pytest_addoption(parser):
    parser.addoption("--dataset", action="store", help="dataset to test")


def pytest_generate_tests(metafunc):
    if "dataset" in metafunc.fixturenames:
        if metafunc.config.option.dataset is None:
            metafunc.parametrize("dataset", ["htqc", "cellpainting"], indirect=True)
        else:
            assert metafunc.config.option.dataset in ["htqc", "cellpainting"]

            metafunc.parametrize("dataset", [metafunc.config.option.dataset], indirect=True)


@pytest.fixture
def dataset(request):
    if request.param == "htqc":
        return {
            "data_dir": "tests/data_a",
            "munged_dir": "tests/data_a_munged",
            "row_counts":
                {
                    "n_plates": 1,
                    "n_channels": 3,
                    "n_channels_raddist": 3,
                    "n_patterns": 3,
                    "n_wells": 4,
                    "n_images": 8,
                    "n_objects": 40,
                    "n_bins_raddist": 4,
                    "n_scales_texture": 3,
                    "n_scales_neighborhood": 2,
                    "n_moments_coefs": 30,
                    "n_correlation_pairs": 5
                },
            "ingest":
                {
                    "image_nrows": 8,
                    "image_ncols": 229,
                    "Cells_nrows": 40,
                    "Cells_ncols": 294,
                    "Cytoplasm_nrows": 40,
                    "Cytoplasm_ncols": 279,
                    "Nuclei_nrows": 40,
                    "Nuclei_ncols": 287
                },
            "munge": True
        }

    if request.param == "cellpainting":
        return {
            "data_dir": "tests/data_b",
            "row_counts":
                {
                    "n_plates": 1,
                    "n_channels": 5,
                    "n_channels_raddist": 4,
                    "n_patterns": 3,
                    "n_wells": 2,
                    "n_images": 4,
                    "n_objects": 40,
                    "n_bins_raddist": 4,
                    "n_scales_texture": 3,
                    "n_scales_neighborhood": 2,
                    "n_moments_coefs": 30,
                    "n_correlation_pairs": 10
                },
            "ingest":
                {
                    "Image_nrows": 4,
                    "Image_ncols": 6,
                    "Cells_nrows": 40,
                    "Cells_ncols": 586,
                    "Cytoplasm_nrows": 40,
                    "Cytoplasm_ncols": 572,
                    "Nuclei_nrows": 40,
                    "Nuclei_ncols": 595
                },
            "munge": False
        }

    raise ValueError("No such dataset: {}".format(request.param))
