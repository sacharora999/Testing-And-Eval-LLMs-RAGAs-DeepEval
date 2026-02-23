from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric

answer_relevancy_met =  AnswerRelevancyMetric()
test_case = LLMTestCase(
    input="Who is the current prsident of USA ?",
    actual_output="Donald Trump",
    retrieval_context=["Donald Trump is the current president of the USA"]
)

answer_relevancy_met.measure(test_case)
print(answer_relevancy_met.score)
