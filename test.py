from pattern_match import task1, common_regex, matching
from pattern_match.error_patterns import errors1, errors2
from util import test_util
from pattern_match.patterns.task2 import goal1 as t2g1
from pattern_match.patterns.task2 import goal2 as t2g2
from pattern_match.patterns.task2 import goal3 as t2g3


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
    t2g2.test_he_is_a_cook()
    t2g3.test_she_is_a_job()
    t2g3.test_my_mother_is_a_job()
    errors2.test_wrong_subject()
    errors2.test_capitalized_doctor()
    errors2.test_wrong_job_1()
    errors2.test_wrong_subject2()
    errors2.test_capitalized_cook()
    errors2.test_wrong_job_2()
    errors2.test_capitalized_mother()


    print('\n\n%s/%s with errors.' %
          (test_util.ERROR_COUNT, test_util.COUNT))
