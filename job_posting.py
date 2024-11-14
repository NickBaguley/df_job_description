import sys
from job_posting.crew import JobPostingCrew

def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'company_domain':'www.dfdancestudio.com/about',
        'company_description': "Utah largest SALSA, BACHATA, SWING, COUNTRY and BALLROOM Dance Studio for adults since 2008! Adult Dance Classes in Salt Lake City Utah in Salsa, Bachata, West Coast Swing, Country Swing, Social Ballroom, and Wedding Ballroom Dances.",
        'hiring_needs': 'Master Dance Teacher, for Latin Dancing that can lead teachers, develop curriculum, build and train syllabuses, and grow the studios offerings.',
        'specific_benefits':'Semi-Monthly Pay, competitive salary, healthcare',
    }
    JobPostingCrew().crew().kickoff(inputs=inputs)



def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'company_domain':'www.dfdancestudio.com/about',
        'company_description': "Utah largest SALSA, BACHATA, SWING, COUNTRY and BALLROOM Dance Studio for adults since 2008! Adult Dance Classes in Salt Lake City Utah in Salsa, Bachata, West Coast Swing, Country Swing, Social Ballroom, and Wedding Ballroom Dances.",
        'hiring_needs': 'Master Dance Teacher, for Latin Dancing that can lead teachers, develop curriculum, build and train syllabuses, and grow the studios offerings.',
        'specific_benefits':'Semi-Monthly Pay, competitive salary, healthcare',
    }
    try:
        JobPostingCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")
