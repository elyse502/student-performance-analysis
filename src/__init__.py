"""
Student Performance Analysis - Source Package

This package contains modules and utilities for the student performance analysis project.
It follows Python package conventions for maintainable, importable code.

Author: Elysée NIYIBIZI
Date: 2026-06-01
"""

__version__ = "1.0.0"
__author__ = "Elysée Niyibizi"
__email__ = "elyseniyibizi502@gmail.com"
__description__ = "Student Performance Analysis and Predictive Modeling"

# Package metadata for future package distribution
PACKAGE_INFO = {
    "name": "student-performance-analysis",
    "version": __version__,
    "author": __author__,
    "description": "A comprehensive data analysis project examining factors influencing student academic performance",
    "keywords": ["education", "data-science", "analysis", "machine-learning", "predictive-modeling"],
    "license": "MIT",
    "python_requires": ">=3.8",
}

# Import paths for future modules (commented until modules are created)
# When you add modules to src/, uncomment and update these imports

# Data loading and preprocessing utilities
# from .data_loader import load_student_data, clean_student_data
# from .preprocessing import preprocess_features, encode_categorical

# Analysis and visualization utilities
# from .analysis import analyze_performance, calculate_correlations
# from .visualization import create_performance_charts, plot_correlations

# Modeling utilities (for future ML implementation)
# from .modeling import train_model, evaluate_model, predict_grades

# Utility functions
# from .utils import save_results, load_config, validate_data

# Export commonly used functions (will be populated as modules are created)
__all__ = [
    # Data functions
    # 'load_student_data',
    # 'clean_student_data',
    
    # Analysis functions  
    # 'analyze_performance',
    # 'calculate_correlations',
    
    # Visualization functions
    # 'create_performance_charts',
    # 'plot_correlations',
    
    # Modeling functions
    # 'train_model',
    # 'evaluate_model',
    # 'predict_grades',
    
    # Utility functions
    # 'save_results',
    # 'load_config',
    # 'validate_data',
]

# Package initialization message
def _print_welcome():
    """Print welcome message when package is imported."""
    welcome_msg = f"""
    {'='*60}
    Student Performance Analysis Package v{__version__}
    {'='*60}
    
    Welcome to the student performance analysis project!
    
    This package provides tools for:
    • Loading and preprocessing student performance data
    • Analyzing academic performance patterns
    • Visualizing key insights and relationships
    • Building predictive models for grade forecasting
    
    Author: {__author__}
    Status: Analysis Complete | ML Modeling Pending
    
    For usage examples, see the notebooks/ directory.
    For documentation, see the README.md file.
    {'='*60}
    """
    return welcome_msg

# Print welcome message on import (optional - can be commented out)
# print(_print_welcome())

# Add custom exceptions for better error handling
class StudentDataError(Exception):
    """Base exception for student data related errors."""
    pass


class DataValidationError(StudentDataError):
    """Raised when data fails validation checks."""
    pass


class MissingDataError(StudentDataError):
    """Raised when required data is missing."""
    pass


class ModelTrainingError(StudentDataError):
    """Raised when model training fails."""
    pass


# Configuration defaults (can be moved to config.py later)
DEFAULT_CONFIG = {
    "data_paths": {
        "raw": "data/raw/student_performance.csv",
        "cleaned": "data/cleaned/student_performance_cleaned.csv",
    },
    "analysis_settings": {
        "target_column": "g3",
        "grade_columns": ["g1", "g2", "g3"],
        "categorical_columns": [
            "school", "sex", "address", "famsize", "pstatus", 
            "mjob", "fjob", "reason", "guardian", "schoolsup",
            "famsup", "paid", "activities", "nursery", "higher",
            "internet", "romantic"
        ],
        "numerical_columns": [
            "age", "medu", "fedu", "traveltime", "studytime",
            "failures", "famrel", "freetime", "goout", "dalc",
            "walc", "health", "absences", "g1", "g2", "g3"
        ],
    },
    "modeling_settings": {
        "test_size": 0.2,
        "random_state": 42,
        "cv_folds": 5,
    }
}

# Utility function placeholder for future development
def get_package_info():
    """Return package information dictionary."""
    return PACKAGE_INFO.copy()

def get_default_config():
    """Return a copy of the default configuration."""
    import copy
    return copy.deepcopy(DEFAULT_CONFIG)

# Package initialization logging (optional)
import logging

# Configure package-level logger
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())  # Default no-op handler

def setup_logging(level=logging.INFO):
    """
    Set up basic logging for the package.
    
    Parameters:
    -----------
    level : int
        Logging level (default: logging.INFO)
    """
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    logger.info(f"Student Performance Analysis package initialized (v{__version__})")

# Add __main__ block for testing the package
if __name__ == "__main__":
    print(_print_welcome())
    print("\nPackage Information:")
    for key, value in get_package_info().items():
        print(f"  {key}: {value}")
    
    print("\nDefault Configuration Available:")
    config = get_default_config()
    print(f"  • Data paths: {len(config['data_paths'])} configured")
    print(f"  • Analysis settings: {len(config['analysis_settings']['categorical_columns'])} categorical columns")
    print(f"  • Modeling settings: Test size = {config['modeling_settings']['test_size']}")
    
    print("\n✅ Package structure verified and ready for development!")