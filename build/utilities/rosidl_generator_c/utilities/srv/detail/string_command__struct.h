// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from utilities:srv/StringCommand.idl
// generated code does not contain a copyright notice

#ifndef UTILITIES__SRV__DETAIL__STRING_COMMAND__STRUCT_H_
#define UTILITIES__SRV__DETAIL__STRING_COMMAND__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'command'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/StringCommand in the package utilities.
typedef struct utilities__srv__StringCommand_Request
{
  rosidl_runtime_c__String command;
} utilities__srv__StringCommand_Request;

// Struct for a sequence of utilities__srv__StringCommand_Request.
typedef struct utilities__srv__StringCommand_Request__Sequence
{
  utilities__srv__StringCommand_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} utilities__srv__StringCommand_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'answer'
// already included above
// #include "rosidl_runtime_c/string.h"

/// Struct defined in srv/StringCommand in the package utilities.
typedef struct utilities__srv__StringCommand_Response
{
  rosidl_runtime_c__String answer;
} utilities__srv__StringCommand_Response;

// Struct for a sequence of utilities__srv__StringCommand_Response.
typedef struct utilities__srv__StringCommand_Response__Sequence
{
  utilities__srv__StringCommand_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} utilities__srv__StringCommand_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // UTILITIES__SRV__DETAIL__STRING_COMMAND__STRUCT_H_
