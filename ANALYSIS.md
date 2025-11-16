# Week 8: Analysis on Data Poisoning

This document addresses the mitigation of data poisoning attacks and the relationship between data quantity and quality.

## 1. Validation Outcomes (Observed in MLflow)

After running the experiments, the MLflow UI will show a clear trend:

* **`poison_rate` = 0.0 (Baseline):** Accuracy will be high (e.g., ~0.95-0.98). This is our clean, trusted model.
* **`poison_rate` = 0.05 (5%):** Accuracy will see a noticeable drop. The model is starting to learn incorrect patterns from the 5% of flipped labels.
* **`poison_rate` = 0.10 (10%):** Accuracy will drop more significantly. The "noise" from the poisoned data is now strong enough to confuse the model's decision boundaries.
* **`poison_rate` = 0.50 (50%):** Accuracy will plummet to a level equivalent to (or worse than) random guessing. With half the labels being intentionally wrong, the model cannot learn any meaningful relationship between the features (petal length, etc.) and the species. The signal is completely lost in the noise.

## 2. Mitigating Data Poisoning Attacks

Data poisoning is a serious threat, especially when models are trained on user-generated or web-scraped data. Here are several strategies for mitigation:

* **Data Validation and Sanitization:** This is the first line of defense.

  * **Outlier Detection:** Implement statistical checks (e.g., using Z-scores or Isolation Forests) to flag data points that are far outside the expected distribution (e.g., a petal length of 500cm).
  * **Label Consistency Checks:** For new data, check if similar feature sets are producing wildly different labels. If 10 samples with nearly identical features have a `setosa` label, a new, similar sample labeled `virginica` is suspicious.
* **Data Provenance:** Know where your data comes from.

  * Use trusted, verified sources whenever possible.
  * If using user-generated content, require authentication and track contributions to identify and block malicious actors.
* **Robust Training Methods:**

  * **Ensemble Methods (e.g., Bagging):** Train multiple models on different random subsets (bags) of the training data. A small number of poisoned samples will only affect a few of the models, and their incorrect predictions can be "outvoted" by the majority of clean models.
  * **Data Slicing Validation:** Don't rely on a single, global accuracy metric. Validate your model's performance on known, clean slices of your data. If the model performs well on the clean slice but poorly overall, it's a sign that the new data may be compromised.
* **Data-Cleaning Tools:** Use data-centric AI tools (e.g., Cleanlab) that are specifically designed to find and correct label errors in a dataset, which is effectively what our "poisoned" data points are.

## 3. Data Quantity vs. Data Quality

This experiment highlights a fundamental concept in MLOps: **Quality is almost always more important than quantity.**

* **Impact of Poor Quality:** As demonstrated, adding low-quality (poisoned) data *actively harms* the model. A model trained on 10,000 samples with 50% incorrect labels will be useless. A model trained on 100 *perfectly* clean samples will be highly accurate.
* **Evolving Data Quantity Requirements:**

  * When data quality is **high**, adding more data (quantity) generally leads to better generalization and a more robust model.
  * When data quality is **low**, you need a **vastly larger amount of data** to compensate. The "signal" (correct data) must be strong enough to drown out the "noise" (bad data). If 10% of your data is noise, you need significantly more than 10% *new, clean data* to overcome the damage.
  * This creates a difficult cycle: more bad data requires even *more* good data, increasing costs for collection and verification. It is often far more cost-effective to **invest in cleaning and verifying a smaller dataset** than to blindly collect massive, noisy datasets.
