def solution(balls, share):
    n_fac, m_fac, nm_fac = 1, 1, 1
    
    for i in range(1, balls+1):
        n_fac *= i
    
    for i in range(1, share+1):
        m_fac *= i
    
    for i in range(1, (balls-share)+1):
        nm_fac *= i
        
    return  n_fac // (nm_fac * m_fac)