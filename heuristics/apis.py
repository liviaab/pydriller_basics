import re

def count_pattern_in_content(pattern, content):
	return len(re.findall(pattern, content))

class UnittestAPIHeuristics:
	testCaseSubclass_pattern = "\(.*TestCase\)"
	assert_pattern = "self.assert.*\("
	setUp_pattern = "def\s+setUp\("
	setUpClass_pattern = "def\s+setUpClass\("
	tearDown_pattern = "def\s+tearDown\("
	tearDownClass_pattern = "def\s+tearDownClass\("
	skipTest_pattern = "@unittest.skip.*\(|self.skipTest"
	expectedFailure_pattern = "@unittest.expectedFailure"

	@classmethod
	def count_apis(cls, content):
		quantity_by_api = {
			"testCaseSubclass": count_pattern_in_content(testCaseSubclass_pattern, content),
			"assert": count_pattern_in_content(assert_pattern, content),
			"setUp": count_pattern_in_content(setUp_pattern, content),
			"setUpClass": count_pattern_in_content(setUpClass_pattern, content),
			"tearDown": count_pattern_in_content(tearDown_pattern, content),
			"tearDownClass": count_pattern_in_content(tearDownClass_pattern, content),
			"skipTest": count_pattern_in_content(skipTest_pattern, content),
			"expectedFailure": count_pattern_in_content(expectedFailure_pattern, content)
		}

		return quantity_by_api


class PytestAPIHeuristics:
	assert_pattern = "\s*assert\s+"
	raiseError_pattern = "\s*raise\s+|pytest.raises\("
	skipTest_pattern = "pytest.skip\(|@pytest.mark.skip\(|@pytest.mark.skipIf\("
	expectedFailure_pattern = "@pytest.mark.xfail|pytest.xfail\("
	fixture_pattern = "@pytest.mark.usefixtures\(|@pytest.fixture"

	@classmethod
	def count_apis(cls, content):
		quantity_by_api = {
			"assert": count_pattern_in_content(assert_pattern, content),
			"raiseError": count_pattern_in_content(raiseError_pattern, content),
			"skipTest": count_pattern_in_content(skipTest_pattern, content),
			"expectedFailure": count_pattern_in_content(expectedFailure_pattern, content),
			"fixture": count_pattern_in_content(fixture_pattern, content),
		}

		return quantity_by_api