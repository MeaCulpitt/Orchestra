# orchestra/validator/reward.py

def calculate_combined_score(routing_score, standardization_score, weights=[0.7, 0.3]):
    """
    Calculates a miner's final epoch incentive by combining the 
    Task Routing and JSON Standardization mechanisms.
    """
    # Mechanism 0: Routing & Synthesis (70%)
    m0_weighted = routing_score * weights[0]
    
    # Mechanism 1: Data Standardization (30%)
    # This involves Pydantic validation and schema matching checks
    m1_weighted = standardization_score * weights[1]
    
    # Final Incentive used for weight setting
    final_incentive = m0_weighted + m1_weighted
    
    return final_incentive

# Example: Miner gets 0.9 on routing but 0.4 on JSON formatting
# Final Score: (0.9 * 0.7) + (0.4 * 0.3) = 0.63 + 0.12 = 0.75
