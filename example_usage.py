from client import ConversationalBrandAgentSafetyGuardrailGovernorClient

def main():
    client = ConversationalBrandAgentSafetyGuardrailGovernorClient()
    res = client.enforce_brand_conversational_guardrails('GLOBAL_RETAIL_BANKING_AGENT')
    print('Guardrail Eval: ' + res['guardrail_evaluation_id'] + ' for ' + res['brand_id'])
    print('Action Taken: ' + res['deterministic_business_action_taken'] + ' (Latency: ' + str(res['voice_and_chat_latency_ms']) + 'ms)')
    print('Prompt Leak Blocked: ' + str(res['system_prompt_leak_attempt_blocked']) + ' | Policy Adherence: ' + str(res['policy_adherence_score_pct']) + '%')

if __name__ == '__main__':
    main()
