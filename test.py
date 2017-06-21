from pattern_match import task1, common_regex, matching
from pattern_match.error_patterns import errors1, errors2
from util import test_util
from pattern_match.patterns.task2 import goal1 as t2g1


if __name__ == '__main__':
    common_regex.test_name()
    common_regex.test_number()
    common_regex.test_ordinal()
    task1.test_match_name()
    task1.test_match_nice_to_meet_you()
    task1.test_match_how_are_you_response()
    task1.test_match_where_are_your_from_response()
    task1.test_match_how_old_are_you_response()
    task1.test_match_what_grade_are_you_in_response()
    errors1.test_what_is_your_name()
    errors1.test_nice_to_meet_you()
    errors1.test_how_are_you()
    matching.test_wiring()
    t2g1.test_she_is_a_doctor_match()
    errors2.test_wrong_subject()
    errors2.test_capitalized_doctor()

    print('\n\n%s/%s with errors.' %
          (test_util.ERROR_COUNT, test_util.COUNT))
