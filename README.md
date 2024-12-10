# MATHEMATICAL MODEL OF COLORECTAL CANCER INITIATION  

**UW AMath422 Autumn Course Project**  
**Professor:** Eric Shea-Brown  
**TA:** Rohin Gilman  

---

## Abstract  
Colorectal cancer (CRC) initiation is driven by the accumulation of critical genetic alterations, including the inactivation of tumor suppressor genes (APC and TP53) and the activation of the oncogene KRAS. This study builds upon the foundational stochastic model of Paterson et al., reformulating it into a matrix-based framework to enhance the analysis of mutation dynamics and crypt expansion. By leveraging transition and growth matrices, we model the progression of 32 genotypic states, capturing the selective growth advantages of APC and KRAS mutations. Comparative results demonstrate that while the matrix approach aligns with tau-leaping simulations, it consistently underestimates malignancy probabilities at early ages, highlighting discrepancies attributable to outflow terms and double mutation assumptions. Our findings underscore the utility of matrix methods in elucidating cancer evolution and provide insights into CRC risk modeling, aligning theoretical predictions with observed epidemiological data.

---

## Project Files and Descriptions  
1. **0_COLORECTAL_CANCER_INITIATION.pdf**  
   Final project paper submitted for grading.  

2. **1_CRC_Initiation_master**  
   This folder contains the original C++ code used by Paterson et al. to perform tau-leaping simulations. The `tauleaping_experiments` subfolder includes results from our four tau-leaping general case experiments and two tau-leaping KRAS-neutral simulations.  

3. **2_tau_leaping_python**  
   Our Python implementation of tau-leaping simulations. While the results require further refinement, this represents an important step towards improving the approach in the future.  

4. **3_replicate**  
   This folder contains:  
   - `Figure_2.ipynb`: Code used to replicate Figure 2 from the original paper.  
   - `temp_code`: More detailed scripts for reproducing results using both the equation approach and the matrix approach.  

5. **4_mutation_state_table.csv**  
   A CSV file documenting the 32 distinct genotypic states defined in our matrix approach.  

6. **5_pre.pdf**  
   Case study presentation slides.  

7. **6_final_pre.pdf**  
   Final project presentation slides.  

---

## Authors  
- Yirui Chen, Zihan Chen, Haoran Xiang, Shihong Ding, Yuyue Yuan  

---

## Acknowledgments  
Many thanks for the guidance and support provided during this project.  

---

## References  
Paterson, Chay, Hans Clevers, and Ivana Bozic. “Mathematical Model of Colorectal Cancer Initiation.” *Proceedings of the National Academy of Sciences* 117, no. 34 (August 25, 2020): 20681–88. [https://doi.org/10.1073/pnas.2003771117](https://doi.org/10.1073/pnas.2003771117)  

---
