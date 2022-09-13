from src.jobs import read


def get_unique_job_types(path):
    unique_list = []
    for job in read(path):
        if job["job_type"] not in unique_list:
            unique_list.append(job["job_type"])
    return unique_list


def filter_by_job_type(jobs, job_type):
    list_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            list_jobs.append(job)
    return list_jobs

    # Ou em uma linha
    # return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    unique_list = []
    for job in read(path):
        if job["industry"] not in unique_list and job["industry"] != '':
            unique_list.append(job["industry"])
    return unique_list


def filter_by_industry(jobs, industry):
    list_industry = []
    for job in jobs:
        if job["industry"] == industry:
            list_industry.append(job)
    return list_industry

    # Ou em uma linha
    # return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    bigger_salary = []
    for job in read(path):
        jobs = job["max_salary"]
        if jobs not in bigger_salary and jobs.isdigit():
            bigger_salary.append(int(jobs))
    return max(bigger_salary)


def get_min_salary(path):
    smaller_salary = []
    for job in read(path):
        jobs = job["min_salary"]
        if jobs not in smaller_salary and jobs.isdigit():
            smaller_salary.append(int(jobs))
    return min(smaller_salary)


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("Oops! min_salary or max_salary undefined")
    elif type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError("Oops! type must be str or int")
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("Oops! min_salary cannot bigger than max_salary")
    elif type(salary) != int:
        raise ValueError("Oops! Salary type must be int")
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
