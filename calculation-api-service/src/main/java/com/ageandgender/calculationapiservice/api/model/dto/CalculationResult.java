package com.ageandgender.calculationapiservice.api.model.dto;

import com.ageandgender.calculationapiservice.api.model.enums.CalculationStatus;
import com.ageandgender.calculationapiservice.api.model.enums.Gender;
import com.fasterxml.jackson.annotation.JsonProperty;

import java.io.Serializable;
import java.util.Arrays;

public class CalculationResult implements Serializable {

    private Long calculationId;

    private CalculationStatus calculationStatus;

    private Gender estimatedGender;

    private String estimatedAge;

    private boolean isFace;

    private String image;

    private String errorMessage;

    public CalculationResult(@JsonProperty("calculationId") Long calculationId,
                             @JsonProperty("calculationStatus") CalculationStatus calculationStatus,
                             @JsonProperty("estimatedGender") Gender estimatedGender,
                             @JsonProperty("estimatedAge") String estimatedAge,
                             @JsonProperty("isFace") boolean isFace,
                             @JsonProperty("image") String image,
                             @JsonProperty("errorMessage") String errorMessage) {
        this.calculationId = calculationId;
        this.calculationStatus = calculationStatus;
        this.estimatedGender = estimatedGender;
        this.estimatedAge = estimatedAge;
        this.isFace = isFace;
        this.image = image;
        this.errorMessage = errorMessage;
    }

    public Long getCalculationId() {
        return calculationId;
    }

    public void setCalculationId(Long calculationId) {
        this.calculationId = calculationId;
    }

    public CalculationStatus getCalculationStatus() {
        return calculationStatus;
    }

    public void setCalculationStatus(CalculationStatus calculationStatus) {
        this.calculationStatus = calculationStatus;
    }

    public Gender getEstimatedGender() {
        return estimatedGender;
    }

    public void setEstimatedGender(Gender estimatedGender) {
        this.estimatedGender = estimatedGender;
    }

    public String getEstimatedAge() {
        return estimatedAge;
    }

    public void setEstimatedAge(String estimatedAge) {
        this.estimatedAge = estimatedAge;
    }

    public boolean isFace() {
        return isFace;
    }

    public void setFace(boolean face) {
        isFace = face;
    }

    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }

    public String getErrorMessage() {
        return errorMessage;
    }

    public void setErrorMessage(String errorMessage) {
        this.errorMessage = errorMessage;
    }

    @Override
    public String toString() {
        return "CalculationResult{" +
                "calculationId=" + calculationId +
                ", calculationStatus=" + calculationStatus +
                ", estimatedGender=" + estimatedGender +
                ", estimatedAge=" + estimatedAge +
                ", isFace=" + isFace +
                ", image=" + image +
                ", errorMessage='" + errorMessage + '\'' +
                '}';
    }
}
