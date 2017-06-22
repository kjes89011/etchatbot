from pattern_match import task1, common_regex, matching
from pattern_match.error_patterns import errors1, errors2
from pattern_match.error_patterns import common as common_errors
from util import test_util
from pattern_match.patterns.task2 import goal1 as t2g1
from pattern_match.patterns.task2 import goal2 as t2g2
from pattern_match.patterns.task2 import goal3 as t2g3
from pattern_match.patterns.task2 import goal4 as t2g4
from pattern_match.patterns.task2 import goal5 as t2g5
from pattern_match.patterns.task2 import goal6 as t2g6


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
    errors1.test_where_are_you_from()
    matching.test_wiring()
    t2g1.test_she_is_a_doctor_match()
    t2g2.test_he_is_a_cook()
    t2g3.test_she_is_a_job()
    t2g3.test_my_mother_is_a_job()
    t2g4.test_he_is_a_job()
    t2g4.test_my_father_is_a_job()
    t2g5.test_no_he_is_not()
    t2g6.test_he_is_a_nurse()
    common_errors.test_missing_verb()
    common_errors.test_missing_determiner()
    common_errors.test_wrong_determiner()
    errors2.test_wrong_subject()
    errors2.test_capitalized_doctor()
    errors2.test_wrong_job_1()
    errors2.test_wrong_subject2()
    errors2.test_capitalized_cook()
    errors2.test_wrong_job_2()
    errors2.test_capitalized_mother()
    errors2.test_capitalized_father()
    errors2.test_missing_comma()
    errors2.test_too_short_answer()
    errors2.test_wrong_job_3()

    print('\n\n%s/%s with errors.' %
          (test_util.ERROR_COUNT, test_util.COUNT))
