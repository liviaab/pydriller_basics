def commit_columns(): 
	return [
		"commit_index",
		"author_name",
		"author_email",
		"date",
		"commit_hash",
		"change_set",
		"pytest_in_removed_diffs",
		"has_test_file",
		"unittest_in_code",
		"unittest_in_removed_diffs",
		"pytest_in_code",
		"commit_message"
	]

def repository_columns():
	return [
		"CATEGORY",
		"REPOSITORY_NAME",
		"REPOSITORY_LINK",
		"NOC",
		"NOC_UNITTEST",
		"NOC_PYTEST",
		"NOC_BOTH",
		"OCM",
		"NOA (name)",
		"NOMA (name)",
		"NOMAP (name)",
		"NOA (email)",
		"NOMA (email)",
		"NOMAP (email)",
		"NOA email - name",
		"NOD",
		"NOF",
		"NOF_UNITTEST",
		"NOF_PYTEST",
		"NOF_BOTH",
		"PBU",
		"FC_UNITTEST",
		"FC_PYTEST",
		"FC_UNITTEST_LINK",
		"FC_PYTEST_LINK",
		"LC_UNITTEST",
		"LC_PYTEST",
		"LC_UNITTEST_LINK",
		"LC_PYTEST_LINK"
	]

def aggregated_columns():
	return [
		'CATEGORY',
		'NOP',
		'NOC - MEAN',
		'NOC - MEDIAN',
		'NOC - MAX',
		'NOC - MIN',

		'NOC_UNITTEST - MEAN',
		'NOC_UNITTEST - MEDIAN',
		'NOC_UNITTEST - MAX',
		'NOC_UNITTEST - MIN',

		'NOC_PYTEST - MEAN',
		'NOC_PYTEST - MEDIAN',
		'NOC_PYTEST - MAX',
		'NOC_PYTEST - MIN',

		'NOC_BOTH - MEAN',
		'NOC_BOTH - MEDIAN',
		'NOC_BOTH - MAX',
		'NOC_BOTH - MIN',

		'NOF - MEAN',
		'NOF - MEDIAN',
		'NOF - MAX',
		'NOF - MIN',

		'NOF_UNITTEST - MEAN',
		'NOF_UNITTEST - MEDIAN',
		'NOF_UNITTEST - MAX',
		'NOF_UNITTEST - MIN',

		'NOF_PYTEST - MEAN',
		'NOF_PYTEST - MEDIAN',
		'NOF_PYTEST - MAX',
		'NOF_PYTEST - MIN',

		'NOF_BOTH - MEAN',
		'NOF_BOTH - MEDIAN',
		'NOF_BOTH - MAX',
		'NOF_BOTH - MIN',
	]